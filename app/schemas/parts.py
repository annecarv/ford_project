from pydantic import BaseModel
from typing import Optional

class PartCreate(BaseModel):
    part_name: str
    supplier_id: int
    last_id_purchance: Optional[int] = None

    class Config:
        orm_mode = True

class PartOut(PartCreate):
    part_id: int

    class Config:
        orm_mode = True
