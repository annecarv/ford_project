from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import conn
from app.schemas.vehicles import VehicleCreate, VehicleOut
from app.db.models import DimWarranty