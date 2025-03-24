from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from app.db.session import engine, Base
from app.db.models import (
    DimLocations, DimSupplier, DimVehicle, DimPart, DimPurchance, FactWarranty, 
    PurchanceType
)

Base.metadata.create_all(engine)
session = Session(bind=engine)

def seed_data(model, data):
    try:
        if not session.query(model).first(): 
            session.add_all(data)
            session.commit()
            print(f'Dados inseridos na tabela {model.__name__}.')
        else:
            print(f'Dados já existentes na tabela {model.__name__}.')
    except IntegrityError as e:
        session.rollback()
        print(f'Erro de integridade ao inserir {model.__name__}: {e}')
    except Exception as e:
        session.rollback()
        print(f'Erro ao inserir {model.__name__}: {e}')

locations = [
    DimLocations(market="América do Norte", country="EUA", province="Califórnia", city="Los Angeles"),
    DimLocations(market="América do Norte", country="EUA", province="Nova York", city="Nova York"),
    DimLocations(market="Europa", country="Alemanha", province="Baviera", city="Munique"),
    DimLocations(market="Ásia", country="Japão", province="Tóquio", city="Tóquio"),
]
seed_data(DimLocations, locations)

location_ids = {loc.city: loc.location_id for loc in session.query(DimLocation).all()}

suppliers = [
    DimSupplier(supplier_name="AutoParts Inc.", location_id=1),
    DimSupplier(supplier_name="Bavaria Motors", location_id=2),
    DimSupplier(supplier_name="Tokyo Auto Parts", location_id=3),
    DimSupplier(supplier_name="Global Car Supply", location_id=4),
]

seed_data(DimSupplier, suppliers)

supplier_ids = {sup.supplier_name: sup.supplier_id for sup in session.query(DimSupplier).all()}

vehicles = [
    DimVehicle(model="Tesla Model S", prod_date=datetime(2023, 5, 10), year=2023, propulsion=PropulsionType.eletric),
    DimVehicle(model="BMW X5", prod_date=datetime(2022, 8, 15), year=2022, propulsion=PropulsionType.hybrid),
    DimVehicle(model="Toyota Corolla", prod_date=datetime(2021, 11, 20), year=2021, propulsion=PropulsionType.gas),
    DimVehicle(model="Audi e-tron", prod_date=datetime(2024, 1, 5), year=2024, propulsion=PropulsionType.eletric),
]
seed_data(DimVehicle, vehicles)

vehicle_ids = {veh.model: veh.vehicle_id for veh in session.query(DimVehicle).all()}

parts = [
    DimPart(part_name="Bateria Elétrica", supplier_id=1),
    DimPart(part_name="Motor Híbrido", supplier_id=2),
    DimPart(part_name="Filtro de Óleo", supplier_id=3),
    DimPart(part_name="Sistema de Freios", supplier_id=4),
]

seed_data(DimPart, parts)

part_ids = {part.part_name: part.part_id for part in session.query(DimPart).all()}

purchances = [
    DimPurchance(purchance_type=PurchanceType.bulk, last_id_purchase=1, purchance_date=datetime(2023, 6, 1)),
    DimPurchance(purchance_type=PurchanceType.warranty, last_id_purchase=2, purchance_date=datetime(2022, 9, 10)),
    DimPurchance(purchance_type=PurchanceType.bulk, last_id_purchase=3, purchance_date=datetime(2021, 12, 15)),
    DimPurchance(purchance_type=PurchanceType.warranty, last_id_purchase=4, purchance_date=datetime(2024, 2, 20)),
]
seed_data(DimPurchance, purchances)

purchance_ids = {purch.last_id_purchase: purch.purchance_id for purch in session.query(DimPurchance).all()}

warranties = [
    FactWarranty(
        vehicle_id=vehicle_ids["Tesla Model S"],
        repair_date=datetime(2024, 3, 1),
        client_comment="Carro parou de funcionar", 
        tech_comment="Defeito na bateria",
        part_id=part_ids["Bateria Elétrica"],
        classifed_failured="Elétrico",
        location_id=location_ids["Los Angeles"],
        purchance_id=purchance_ids[1]
    ),
    FactWarranty(
        vehicle_id=vehicle_ids["BMW X5"],
        repair_date=datetime(2023, 11, 15),
        client_comment="Ruído estranho no motor", 
        tech_comment="Falha na bomba de óleo",
        part_id=part_ids["Motor Híbrido"],
        classifed_failured="Mecânico",
        location_id=location_ids["Nova York"],
        purchance_id=purchance_ids[2]
    )
]
seed_data(FactWarranty, warranties)

#session.close()
