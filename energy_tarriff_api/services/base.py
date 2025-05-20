from typing import Generic, TypeVar
from energy_tarriff_api.crud.base import CRUDRepository

ModelType = TypeVar("ModelType")

class BaseService(Generic[ModelType]):
    def __init__(self, crud_repo: CRUDRepository[ModelType]):
        self.crud_repo = crud_repo
