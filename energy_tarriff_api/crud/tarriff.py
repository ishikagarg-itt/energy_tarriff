from .base import CRUDRepository
from models.tarriff import Tarriff

tarriff_crud = CRUDRepository(Tarriff)