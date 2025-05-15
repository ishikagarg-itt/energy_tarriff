from fastapi import FastAPI
from schemas.Tarriff import Tarriff
from fastapi.responses import JSONResponse
from fastapi import APIRouter, Depends, Body
from services.tarriff_service import TarriffService
from services.dependencies import get_tarriff_service

router = APIRouter()

@router.post("/")
async def fetch_tarriff_data(body: Tarriff = Body(...), service: TarriffService = Depends(get_tarriff_service)):
    data = await service.fetch_tarriff_data(body.model_dump())
    return JSONResponse(content=data)