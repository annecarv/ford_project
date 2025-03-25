from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from app.db.session import SessionLocal, engine, Base
from app.db.models import DimVehicle, DimSupplier, DimPart, DimLocations, DimPurchance, FactWarranty, Propulsion, PurchanceType

session = SessionLocal(bind=engine)
Base.metadata.create_all(bind=engine)

def create_table(data):
    try:
        session.add_all(data)
        session.commit()
    except IntegrityError as e:
        print(e)
        session.rollback()

location1 = DimLocations(market="North America", country="USA", province="California", city="Los Angeles")
location2 = DimLocations(market="Europe", country="Germany", province="Bavaria", city="Munich")

create_table([location1, location2])

supplier1 = DimSupplier(supplier_name="A", location_id=location1.location_id)
supplier2 = DimSupplier(supplier_name="B", location_id=location2.location_id)

create_table([supplier1, supplier2])

part1 = DimPart(part_name="Bateria Elétrica", last_id_purchance=1, supplier_id=supplier1.supplier_id)
part2 = DimPart(part_name="Motor Híbrido", last_id_purchance=2, supplier_id=supplier2.supplier_id)

create_table([part1, part2])

vehicles = [
    DimVehicle(model="Tesla", prod_date=date(2022, 1, 1), year=2022, propulsion='electric'),
    DimVehicle(model="Toyota Prius", prod_date=date(2022, 6, 1), year=2022, propulsion='hybrid'),
    DimVehicle(model="Ford Mustang GT", prod_date=date(2021, 1, 1), year=2021, propulsion='gas'),
]

create_table(vehicles)

purchances = [
    DimPurchance(purchance_type='bulk', purchance_date=date(2022, 1, 1), part_id=part1.part_id),
    DimPurchance(purchance_type='warranty', purchance_date=date(2023, 5, 10), part_id=part2.part_id),
]

session.add_all(purchances)
session.commit()

create_table(purchances)

warranty1 = FactWarranty(
    vehicle_id=vehicles[0].vehicle_id, repair_date=date(2022, 3, 15), client_comment="Defeito no motor", 
    tech_comment="Troca do motor", part_id=part1.part_id, classifed_failured="Failure", 
    location_id=location1.location_id, purchance_id=purchances[0].purchance_id
)

warranty2 = FactWarranty(
    vehicle_id=vehicles[1].vehicle_id, repair_date=date(2022, 6, 20), client_comment="Problema na bateria", 
    tech_comment="Substituição da bateria", part_id=part2.part_id, classifed_failured="Failure", 
    location_id=location2.location_id, purchance_id=purchances[1].purchance_id
)

create_table([warranty1, warranty2])
