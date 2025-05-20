from .base import CRUDRepository
from energy_tarriff_api.models.tarriff import Tarriff

tarriff_crud = CRUDRepository(Tarriff)