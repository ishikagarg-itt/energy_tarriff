import httpx
import os
import pandas as pd
from datetime import datetime
from fastapi import HTTPException
from energy_tarriff_api.services.base import BaseService
from energy_tarriff_api.crud.tarriff import tarriff_crud

class IndependerTarriffService(BaseService):
    API_URL = "https://www.independer.nl/api/energie/zoekresultaat/getzoekresultaat?v=61"

    def __init__(self):
        super().__init__(tarriff_crud)
        self.vendor_mapping = self._get_vendor_mapping()

    async def fetch_tarriff_data(self, request_body: dict) -> dict:
        try:
            data = await self._fetch_data_from_api(request_body)
            tarriffs_data = self._validate_and_extract_products(data)
            self._add_vendor_names(tarriffs_data)
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

    def _validate_and_extract_products(self, data: dict) -> list:
        products = data.get("products")
        if not isinstance(products, list) or not all(isinstance(item, dict) for item in products):
            raise HTTPException(status_code=500, detail="Invalid format: expected list of dictionaries in 'products'")
        return products

    def _add_vendor_names(self, tarriffs: list[dict]) -> None:
        for item in tarriffs:
            maatschappij_id = item.get("maatschappijId")
            item["vendorName"] = self.vendor_mapping.get(maatschappij_id, "Unknown Vendor")

    def _export_to_csv(self, tarriffs: list[dict]) -> None:
        df = pd.json_normalize(tarriffs, sep="_")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"tarriff_data_{timestamp}.csv"
        base_dir = os.path.dirname(os.path.abspath(__file__))
        export_dir = os.path.join(base_dir, "exports_independer")
        os.makedirs(export_dir, exist_ok=True)
        file_path = os.path.join(export_dir, file_name)
        df.to_csv(file_path, index=False, encoding="utf-8")

    def _get_vendor_mapping(self) -> dict:
        return {
            79: "Cool Blue Energy",
            4: "Budget Energy",
            75: "Vattenfall",
            35: "Oxxio",
            44: "Vandebron",
            89: "Engie",
            10: "Eneco",
            17: "Greenchoice",
            39: "Pure Energy",
            86: "Mega",
            82: "Innova Energy",
            43: "United Consumers",
            45: "Free Name",
            24: "Unive via Greenchoice",
            90: "Next Energy",
            24: "Just Energy",
            78: "Frank Energy",
            88: "Clean Energy",
            91: "Tibber",
            80: "North Energy",
            92: "Solar Plan",
            96: "Hello Current",
            70: "At | New Energy",
            36: "Powerpeers",
            95: "Frank Energy Dynamic"
        }

