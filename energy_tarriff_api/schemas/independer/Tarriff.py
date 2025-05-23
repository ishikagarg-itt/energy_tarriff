from pydantic import BaseModel
from .ContractWishes import ContractWishes
from .Address import Address
from .Consumption import Consumption
from typing import Optional

class Tarriff(BaseModel):
    contractWensen: ContractWishes
    adres: Address
    verbruik: Consumption
    creditDiscount: bool
