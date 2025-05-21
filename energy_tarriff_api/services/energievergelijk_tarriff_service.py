import httpx
import os
import pandas as pd
from datetime import datetime
from fastapi import HTTPException
from energy_tarriff_api.services.base import BaseService
from energy_tarriff_api.crud.tarriff import tarriff_crud

class EnergievergelijkTarriffService(BaseService):
    API_URL = "https://api.energievergelijk.nl/vergelijker/search"

    def __init__(self):
        super().__init__(tarriff_crud)

    async def fetch_tarriff_data(self, request_body: dict) -> dict:
        try:
            data = await self._fetch_data_from_api(request_body)
            tarriffs_data = self._validate_data(data)
            self._export_to_csv(tarriffs_data)

            return tarriffs_data

        except httpx.RequestError as exc:
            raise HTTPException(status_code=503, detail=f"API request error: {exc}")
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code, detail=exc.response.text)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error writing CSV: {e}")
        
    async def _fetch_data_from_api(self, request_body: dict) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(self.API_URL, json=request_body)
            response.raise_for_status()
            return response.json()

    def _validate_data(self, data: list) -> list:
        if not isinstance(data, list) or not all(isinstance(item, dict) for item in data):
            raise HTTPException(status_code=500, detail="Invalid format: expected list of dictionaries in 'products'")
        return data

    def _export_to_csv(self, tarriffs: list[dict]) -> None:
        df = pd.json_normalize(tarriffs, sep="_")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"tarriff_data_{timestamp}.csv"
        base_dir = os.path.dirname(os.path.abspath(__file__))
        export_dir = os.path.join(base_dir, "exports_energievergelijk")
        os.makedirs(export_dir, exist_ok=True)
        file_path = os.path.join(export_dir, file_name)
        df.to_csv(file_path, index=False, encoding="utf-8")