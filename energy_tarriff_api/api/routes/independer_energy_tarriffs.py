from energy_tarriff_api.schemas.independer.Tarriff import Tarriff
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, Body
from energy_tarriff_api.services.independer_tarriff_service import IndependerTarriffService
from energy_tarriff_api.services.dependencies import get_independer_tarriff_service

router = APIRouter()

@router.post("/")
async def fetch_tarriff_data(body: Tarriff = Body(...), service: IndependerTarriffService = Depends(get_independer_tarriff_service)):
    data = await service.fetch_tarriff_data(body.model_dump())
    return JSONResponse(content=data)