from fastapi import FastAPI

from api import (energy_tarriff_router)

app = FastAPI(title="Energy Tarriff API", version="0.1.0")

app.include_router(energy_tarriff_router, prefix="/energy-tarriffs", tags=["energy-tarriffs"])