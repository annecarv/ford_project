from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# POST
class WarrantyCreate(BaseModel):
    vehicle_id: int
    repair_date: datetime
    client_comment: Optional[str] = None
    tech_comment: str
    part_id: int
    classifed_failured: str
    location_id: int
    purchance_id: int

# GET
class WarrantyOut(WarrantyCreate):
    claim_key: int
    class Config:
        from_attributes = True  #converte do SQLAlchemy para Pydantic

# PUT/PATCH
class WarrantyUpdate(BaseModel):
    repair_date: Optional[datetime] = None
    client_comment: Optional[str] = None
    tech_comment: Optional[str] = None
    classifed_failured: Optional[str] = None
