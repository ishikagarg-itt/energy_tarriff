from pydantic import BaseModel
from typing import Optional

class ElectricityConsumptionDoubleMeter(BaseModel):
    verbruikDal: int
    verbruikPiek: int
    opwekkingDal: Optional[int] = None
    opwekkingPiek: Optional[int] = None
