from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from typing import List

from database import get_db
from CRUD_operations.CRUD_shipments import create, read_all, read_one_by_id, update_by_id, delete
import schemas

router = APIRouter()


@router.post("/shipments", response_model=schemas.Shipments)
def create_shipment(to_create: schemas.ShipmentsCreate, db: Session = Depends(get_db)):
    """Creates shipments with given data"""
    shipment = create(db, to_create)
    if shipment:
        return shipment 
    else:
        raise RuntimeError("Couldn't create")


@router.get("/shipment/shipment_id}", response_model=schemas.Shipments)
def get_shipment_by_id(shipment_id: int, db: Session = Depends(get_db)):
    """Gets shipment by id"""
    shipment = read_one_by_id(db, shipment_id)
    if shipment:
        return shipment
    else:
        raise RuntimeError("Couldn't get")


@router.get("/shipments", response_model=List[schemas.Shipments])
def get_multiple(offset: int = 0, limit: int = 12, db: Session = Depends(get_db)):
    """Gets multiple shipmentss starting from offset ends on limit"""
    shipments = read_all(db, offset, limit)
    if shipments and len(shipments) > 0:
        return shipments
    else:
        raise RuntimeError("Couldn't get")


@router.put("/shipments/{shipments_id}", response_model=schemas.Shipments)
def update_shipments(shipments_id: int, to_update: schemas.ShipmentsCreate, db: Session = Depends(get_db)):
    """Updates shipments with given data"""
    return update_by_id(db, shipments_id, to_update)


@router.delete("/shipments/{shipments_id}")  # no response
def delete_shipments(shipments_id: int, db: Session = Depends(get_db)):
    """Deletes shipments by its Id"""
    return delete(db, shipments_id)
