from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.models import FactWarranty, DimVehicle, DimPart, DimLocations, DimPurchance
from app.schemas.warranties import WarrantyCreate, WarrantyOut, WarrantyUpdate
from app.db.session import conn
from typing import List
from django.shortcuts import get_object_or_404

router = APIRouter()

@router.post("/warranties/", response_model=WarrantyOut)
def create_warranty(warranty: WarrantyCreate, db: Session = Depends(conn)):

    vehicle = get_object_or_404(db, DimVehicle, warranty.vehicle_id)
    part = get_object_or_404(db, DimPart, warranty.part_id)
    location = get_object_or_404(db, DimLocations, warranty.location_id)
    purchance = get_object_or_404(db, DimPurchance, warranty.purchance_id)

    new_warranty = FactWarranty(
        vehicle_id=warranty.vehicle_id,
        repair_date=warranty.repair_date,
        client_comment=warranty.client_comment,
        tech_comment=warranty.tech_comment,
        part_id=warranty.part_id,
        classifed_failured=warranty.classifed_failured,
        location_id=warranty.location_id,
        purchance_id=warranty.purchance_id
    )

    db.add(new_warranty)
    db.commit()
    db.refresh(new_warranty)

    return new_warranty

@router.get("/warranties/", response_model=List[WarrantyOut])
def get_warranties(db: Session = Depends(conn), skip: int = 0, limit: int = 100):
    warranties = db.query(FactWarranty).offset(skip).limit(limit).all()
    return warranties

@router.get("/warranties/{id}", response_model=WarrantyOut)
def get_warranty(id: int, db: Session = Depends(conn)):
    warranty = db.query(FactWarranty).filter(FactWarranty.claim_key == id).first()
    if warranty is None:
        raise HTTPException(status_code=404, detail="Warranty not found")
    return warranty

@router.put("/warranties/{id}", response_model=WarrantyOut)
def update_warranty(id: int, warranty: WarrantyCreate, db: Session = Depends(conn)):
    db_warranty = db.query(FactWarranty).filter(FactWarranty.claim_key == id).first()
    if db_warranty is None:
        raise HTTPException(status_code=404, detail="Warranty not found")

    db_warranty.repair_date = warranty.repair_date
    db_warranty.client_comment = warranty.client_comment
    db_warranty.tech_comment = warranty.tech_comment
    db_warranty.part_id = warranty.part_id
    db_warranty.classifed_failured = warranty.classifed_failured
    db_warranty.location_id = warranty.location_id
    db_warranty.purchance_id = warranty.purchance_id

    db.commit()
    db.refresh(db_warranty)

    return db_warranty

@router.delete("/warranties/{id}", response_model=WarrantyOut)
def delete_warranty(id: int, db: Session = Depends(conn)):
    warranty = db.query(FactWarranty).filter(FactWarranty.claim_key == id).first()
    if warranty is None:
        raise HTTPException(status_code=404, detail="Warranty not found")

    db.delete(warranty)
    db.commit()

    return warranty

