# services/dependencies.py
from services.tarriff_service import TarriffService

def get_tarriff_service() -> TarriffService:
    return TarriffService()
