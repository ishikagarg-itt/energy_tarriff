from pydantic import BaseModel
from typing import Optional

class ContractWishes(BaseModel):
    contractSoort: str
    doelgroep: int
    extraBiedtDiensten: bool
    extraHelptMetBesparen: bool
    extraHelptMetInzichtInGebruik: bool
    hasSmartMeter: bool
    stroomGroenheid: int
    contractKind: str
    tariffFixedPeriod: Optional[str] = None
