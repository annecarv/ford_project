from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import conn
from app.schemas.vehicles import VehicleCreate, VehicleOut
from app.db.models import DimVehicle

router = APIRouter()

@router.post("/", response_model=VehicleOut)
async def create_vehicle(vehicle: VehicleCreate, db: Session = Depends(conn)):
    db_vehicle = DimVehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

@router.get("/{vehicle_id}", response_model=VehicleOut)
async def get_vehicle(vehicle_id: int, db: Session = Depends(conn)):
    return db.query(DimVehicle).filter(DimVehicle.vehicle_id == vehicle_id).first()
