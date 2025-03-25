from pydantic import BaseModel
from datetime import date
from typing import Optional

# Schema para criação de uma nova garantia (usado no POST)
class WarrantyCreate(BaseModel):
    vehicle_id: int  # Este campo será necessário porque é uma chave estrangeira
    repair_date: date
    client_comment: Optional[str] = None
    tech_comment: str
    part_id: int  # Este campo será necessário porque é uma chave estrangeira
    classifed_failured: str
    location_id: int  # Este campo será necessário porque é uma chave estrangeira
    purchance_id: int  # Este campo será necessário porque é uma chave estrangeira

# Schema para resposta da API (usado no GET)
class WarrantyOut(WarrantyCreate):
    claim_key: int  # ID gerado automaticamente após criação

    class Config:
        from_attributes = True  # Permite converter do SQLAlchemy para Pydantic

# Schema para atualização parcial da garantia (usado no PUT/PATCH)
class WarrantyUpdate(BaseModel):
    repair_date: Optional[date] = None
    client_comment: Optional[str] = None
    tech_comment: Optional[str] = None
    classifed_failured: Optional[str] = None
