from pydantic import BaseModel
from typing import Optional

class Tarriff(BaseModel):
    gasConsumption: Optional[int] = None
    powerConsumption: Optional[int] = None
    solarConsumption: Optional[int] = None
    zipcode: Optional[str] = None
    housenumber: Optional[str] = None
    power_low: Optional[int] = None
    price_rate: str
    filters: Optional[list] = None
    lang: str
