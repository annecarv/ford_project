from typing import List
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import conn
from app.schemas.parts import PartCreate, PartOut
from app.db.models import DimPart

router = APIRouter()

@router.post("/", response_model=PartOut)
async def create_part(part: PartCreate, db: Session = Depends(conn)):
    db_part = DimPart(**part.dict())
    db.add(db_part)
    db.commit()
    db.refresh(db_part)
    return db_part

@router.get("/{part_id}", response_model=PartOut)
async def get_part(part_id: int, db: Session = Depends(conn)):
    db_part = db.query(DimPart).filter(DimPart.part_id == part_id).first()
    if db_part is None:
        raise HTTPException(status_code=404, detail="Part not found")
    return db_part

@router.get("/", response_model=List[PartOut])
async def get_all_parts(db: Session = Depends(conn), skip: int = 0, limit: int = 100):
    parts = db.query(DimPart).offset(skip).limit(limit).all()
    return parts

@router.put("/{part_id}", response_model=PartOut)
async def update_part(part_id: int, part: PartCreate, db: Session = Depends(conn)):
    db_part = db.query(DimPart).filter(DimPart.part_id == part_id).first()
    if db_part is None:
        raise HTTPException(status_code=404, detail="Part not found")

    for key, value in part.dict().items():
        setattr(db_part, key, value)

    db.commit()
    db.refresh(db_part)
    return db_part

@router.delete("/{part_id}", response_model=PartOut)
async def delete_part(part_id: int, db: Session = Depends(conn)):
    db_part = db.query(DimPart).filter(DimPart.part_id == part_id).first()
    if db_part is None:
        raise HTTPException(status_code=404, detail="Part not found")

    db.delete(db_part)
    db.commit()
    return db_part
