from pydantic import BaseModel

class LocationBase(BaseModel):
    market: str
    country: str
    province: str
    city: str

class LocationCreate(LocationBase):
    pass

class LocationOut(LocationBase):
    location_id: int

    class Config:
        orm_mode = True
