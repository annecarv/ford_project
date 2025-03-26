from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import conn
from app.schemas.locations import LocationCreate, LocationOut
from app.db.models import DimLocations

router = APIRouter()

@router.post("/", response_model=LocationOut)
async def create_location(location: LocationCreate, db: Session = Depends(conn)):
    db_location = DimLocations(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

@router.get("/{location_id}", response_model=LocationOut)
async def get_location(location_id: int, db: Session = Depends(conn)):
    db_location = db.query(DimLocations).filter(DimLocations.location_id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location

@router.get("/", response_model=list[LocationOut])
async def get_all_locations(db: Session = Depends(conn)):
    return db.query(DimLocations).all()

@router.put("/{location_id}", response_model=LocationOut)
async def update_location(location_id: int, location: LocationCreate, db: Session = Depends(conn)):
    db_location = db.query(DimLocations).filter(DimLocations.location_id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    for key, value in location.dict().items():
        setattr(db_location, key, value)

    db.commit()
    db.refresh(db_location)
    return db_location

@router.delete("/{location_id}", response_model=LocationOut)
async def delete_location(location_id: int, db: Session = Depends(conn)):
    db_location = db.query(DimLocations).filter(DimLocations.location_id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")

    db.delete(db_location)
    db.commit()
    return db_location
