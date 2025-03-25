from datetime import datetime
from pydantic import BaseModel

class VehicleCreate(BaseModel):
    model: str
    prod_date: datetime
    year: int
    propulsion: str

class VehicleOut(VehicleCreate):
    vehicle_id: int
