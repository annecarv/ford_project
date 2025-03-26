from pydantic import BaseModel
from typing import Optional
from app.schemas.locations import LocationOut

class SupplierBase(BaseModel):
    supplier_name: str
    location_id: int

class SupplierCreate(SupplierBase):
    pass

class SupplierOut(SupplierBase):
    supplier_id: int
    location: LocationOut 

    class Config:
        orm_mode = True
