from typing import Type, TypeVar, Generic
from energy_tarriff_api.log import get_logger

ORMModel = TypeVar("ORMModel")
log = get_logger(__name__)

class CRUDRepository(Generic[ORMModel]):
    def __init__(self, model: Type[ORMModel]) -> None:
        self._model = model
        self._name = model.__name__