from sqlalchemy.orm import Session
from Tables.shipments import Shipments
from sqlalchemy import update
from schemas import ShipmentsCreate
from typing import List, Any


def create(db: Session, shipment: ShipmentsCreate) -> Shipments:
    """Creates shipment"""
    new_shipment = Shipments(
        Date_Of_Shipment=shipment.Date_Of_Shipment,
        Volume_Of_Shipment=shipment.Volume_Of_Shipment,
        Sale_Price=shipment.Sale_Price,

        Enterprise_Id=shipment.Enterprise_Id,
        Products_Id=shipment.Products_Id
    )
    db.add(new_shipment)
    db.commit()
    db.refresh(new_shipment)
    return new_shipment


def read_one_by_id(db: Session, shipment_id: int) -> Shipments | None:
    """Returns shipment with given Id (Primary Key)"""
    return db.query(Shipments).get(shipment_id)


def read_all(db: Session, offset: int = 0, limit: int = 12) -> List[Any]:
    """Returns specific amount of values"""
    return db.query(Shipments).offset(offset).limit(limit).all()


def update_by_id(db: Session, product_id: int, new_shipment: ShipmentsCreate) -> Shipments:
    """Updates shipmnet with given Id with new_shipmnet"""
    to_update = (
        update(Shipments).
        where(Shipments.Id == product_id).
        values(
            Date_Of_Shipment=new_shipment.Date_Of_Shipment,
            Volume_Of_Shipment=new_shipment.Volume_Of_Shipment,
            Sale_Price=new_shipment.Sale_Price,

            Enterprise_Id=new_shipment.Enterprise_Id,
            Products_Id=new_shipment.Products_Id
        )
    )
    db.execute(to_update)
    db.commit()

    return read_one_by_id(db, product_id)


def delete(db: Session, shipment_id: int) -> None:
    """Deletes a shipment with given Id"""
    db.delete(db.query(Shipments).get(shipment_id))
    db.commit()
