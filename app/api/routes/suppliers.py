from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import conn
from app.schemas.suppliers import SupplierCreate, SupplierOut
from app.db.models import DimSupplier

router = APIRouter()

@router.post("/", response_model=SupplierOut)
async def create_supplier(supplier: SupplierCreate, db: Session = Depends(conn)):
    db_supplier = DimSupplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

@router.get("/{supplier_id}", response_model=SupplierOut)
async def get_supplier(supplier_id: int, db: Session = Depends(conn)):
    db_supplier = db.query(DimSupplier).filter(DimSupplier.supplier_id == supplier_id).first()
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@router.get("/", response_model=list[SupplierOut])
async def get_all_suppliers(db: Session = Depends(conn)):
    return db.query(DimSupplier).all()

@router.put("/{supplier_id}", response_model=SupplierOut)
async def update_supplier(supplier_id: int, supplier: SupplierCreate, db: Session = Depends(conn)):
    db_supplier = db.query(DimSupplier).filter(DimSupplier.supplier_id == supplier_id).first()
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    for key, value in supplier.dict().items():
        setattr(db_supplier, key, value)

    db.commit()
    db.refresh(db_supplier)
    return db_supplier

@router.delete("/{supplier_id}", response_model=SupplierOut)
async def delete_supplier(supplier_id: int, db: Session = Depends(conn)):
    db_supplier = db.query(DimSupplier).filter(DimSupplier.supplier_id == supplier_id).first()
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    db.delete(db_supplier)
    db.commit()
    return db_supplier
