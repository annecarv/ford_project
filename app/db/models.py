from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Text, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ENUM
from app.db.session import Base

class Propulsion(Enum):
    electric = 'electric'
    hybrid = 'hybrid'
    gas = 'gas'

class PurchanceType(Enum):
    bulk = 'bulk'
    warranty = 'warranty'

class DimVehicle(Base):
    __tablename__ = 'Dim_Vehicle'

    vehicle_id = Column(Integer, primary_key=True, unique=True)
    model = Column(String(255), nullable=False)
    prod_date = Column(Date, nullable=False)
    year = Column(Integer, nullable=False)
    propulsion = Column(ENUM('electric', 'hybrid', 'gas', name='propulsion_t'), nullable=False)

    warranties = relationship("FactWarranty", back_populates="vehicle")

class DimLocations(Base):
    __tablename__ = 'Dim_Locations'

    location_id = Column(Integer, primary_key=True, autoincrement=True)
    market = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)

    suppliers = relationship("DimSupplier", back_populates="location")
    warranties = relationship("FactWarranty", back_populates="location")

class DimPart(Base):
    __tablename__ = 'Dim_Part'

    part_id = Column(Integer, primary_key=True, autoincrement=True)
    part_name = Column(String(255), nullable=False)
    supplier_id = Column(Integer, ForeignKey('Dim_Supplier.supplier_id'), nullable=False)
    last_id_purchance = Column(Integer, ForeignKey('Dim_Purchance.purchance_id'), nullable=True)

    purchances = relationship(
        "DimPurchance", 
        back_populates="parts", 
        primaryjoin="DimPart.part_id == DimPurchance.part_id",

    )

    last_purchances = relationship(
        "DimPurchance", 
        back_populates="last_purchances", 
        foreign_keys=[last_id_purchance],
        remote_side="DimPurchance.purchance_id"
    )

    suppliers = relationship("DimSupplier", back_populates="parts", foreign_keys=[supplier_id])
    warranties = relationship("FactWarranty", back_populates="parts")

class DimSupplier(Base):
    __tablename__ = 'Dim_Supplier'

    supplier_id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_name = Column(String(50), nullable=False)
    location_id = Column(Integer, ForeignKey('Dim_Locations.location_id'), nullable=False)

    location = relationship("DimLocations", back_populates="suppliers")
    parts = relationship("DimPart", back_populates="suppliers")

class DimPurchance(Base):
    __tablename__ = 'Dim_Purchance'

    purchance_id = Column(Integer, primary_key=True, unique=True)
    purchance_type = Column(ENUM('bulk', 'warranty', name='purchance_type_t'), nullable=False)
    purchance_date = Column(Date, nullable=False)
    part_id = Column(Integer, ForeignKey('Dim_Part.part_id'))  

   
    parts = relationship(
        "DimPart",  
        back_populates="purchances", 
        foreign_keys=[part_id], 
        remote_side="DimPurchance.part_id"
    )

    last_purchances = relationship("DimPart", back_populates="last_purchances", foreign_keys=[DimPart.last_id_purchance])

class FactWarranty(Base):
    __tablename__ = 'Fact_Warranties'

    claim_key = Column(Integer, primary_key=True, autoincrement=True)
    vehicle_id = Column(Integer, ForeignKey('Dim_Vehicle.vehicle_id'), nullable=False)
    repair_date = Column(Date, nullable=False)
    client_comment = Column(Text)
    tech_comment = Column(Text, nullable=False)
    part_id = Column(Integer, ForeignKey('Dim_Part.part_id'), nullable=False)
    classifed_failured = Column(String(50), nullable=False)
    location_id = Column(Integer, ForeignKey('Dim_Locations.location_id'), nullable=False)
    purchance_id = Column(Integer, ForeignKey('Dim_Purchance.purchance_id'), nullable=False)

    vehicle = relationship("DimVehicle", back_populates="warranties")
    parts = relationship("DimPart", back_populates="warranties")
    location = relationship("DimLocations", back_populates="warranties")
