from typing import List
from fastapi import APIRouter, Depends, HTTPException
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

@router.get("/", response_model=List[VehicleOut])
async def get_all_vehicles(db: Session = Depends(conn), skip: int = 0, limit: int = 100):
    vehicles = db.query(DimVehicle).offset(skip).limit(limit).all()
    return vehicles

@router.put("/{vehicle_id}", response_model=VehicleOut)
async def update_vehicle(vehicle_id: int, vehicle: VehicleCreate, db: Session = Depends(conn)):
    db_vehicle = db.query(DimVehicle).filter(DimVehicle.vehicle_id == vehicle_id).first()
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    for key, value in vehicle.dict().items():
        setattr(db_vehicle, key, value)

    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

@router.delete("/{vehicle_id}", response_model=VehicleOut)
async def delete_vehicle(vehicle_id: int, db: Session = Depends(conn)):
    db_vehicle = db.query(DimVehicle).filter(DimVehicle.vehicle_id == vehicle_id).first()
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    db.delete(db_vehicle)
    db.commit()
    return db_vehicle