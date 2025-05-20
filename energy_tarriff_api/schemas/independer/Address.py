from pydantic import BaseModel
from typing import Optional

class Address(BaseModel):
    postcode: str
    huisnummer: int
    huisnummertoevoeging: Optional[str]