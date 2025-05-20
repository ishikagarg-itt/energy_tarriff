# services/dependencies.py
from energy_tarriff_api.services.independer_tarriff_service import IndependerTarriffService
from energy_tarriff_api.services.energievergelijk_tarriff_service import EnergievergelijkTarriffService

def get_independer_tarriff_service() -> IndependerTarriffService:
    return IndependerTarriffService()

def get_energievergelijk_tarriff_service() -> EnergievergelijkTarriffService:
    return EnergievergelijkTarriffService()
