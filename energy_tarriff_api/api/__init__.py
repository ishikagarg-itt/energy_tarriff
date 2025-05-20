from .routes.independer_energy_tarriffs import router as independer_energy_tarriff_router
from .routes.energievergelijk_energy_tarriffs import router as energievergelijk_energy_tarriff_router

__all__ = [
    "independer_energy_tarriff_router",
    "energievergelijk_energy_tarriff_router"
]