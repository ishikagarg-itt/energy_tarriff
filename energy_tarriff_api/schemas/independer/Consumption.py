from pydantic import BaseModel
from .ElectricityConsumptionDoubleMeter import ElectricityConsumptionDoubleMeter

class Consumption(BaseModel):
    gasverbruik: int
    meterSoort: int
    elektriciteitverbruikDubbelMeter: ElectricityConsumptionDoubleMeter