from fastapi import FastAPI

from energy_tarriff_api.api import (independer_energy_tarriff_router, energievergelijk_energy_tarriff_router)

app = FastAPI(title="Energy Tarriff API", version="0.1.0")

app.include_router(independer_energy_tarriff_router, prefix="/independer-energy-tarriffs", tags=["independer-energy-tarriffs"])
app.include_router(energievergelijk_energy_tarriff_router, prefix="/energievergelijk-energy-tarriffs", tags=["energievergelijk-energy-tarriffs"])