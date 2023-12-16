from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from typing import List

from database import get_db
from CRUD_operations.CRUD_enterprise import create, read_all, read_one_by_id, read_one_by_name, update_by_id, delete
import schemas

router = APIRouter()


@router.post("/enterprises", response_model=schemas.Enterprise)
def create_enterprise(to_create: schemas.EnterpriseCreate, db: Session = Depends(get_db)):
    """Creates enterprise with given data"""
    enterprise = create(db, to_create)
    if enterprise:
        return enterprise
    else:
        raise RuntimeError("Couldn't create")


@router.get("/enterprises/{enterprise_id}", response_model=schemas.Enterprise)
def get_enterprise_by_id(enterprise_id: int, db: Session = Depends(get_db)):
    """Gets enterprise by id"""
    enterprise = read_one_by_id(db, enterprise_id)
    if enterprise:
        return enterprise
    else:
        raise RuntimeError("Couldn't get")


@router.get("/enterprises/{enterprise_name}", response_model=schemas.Enterprise)
def get_enterprise_by_name(enterprise_name: str, db: Session = Depends(get_db)):
    """Gets enterprise by name"""
    enterprise = read_one_by_name(db, enterprise_name)
    if enterprise:
        return enterprise
    else:
        raise RuntimeError("Couldn't get")


@router.get("/enterprises", response_model=List[schemas.Enterprise])
def get_multiple(offset: int = 0, limit: int = 12, db: Session = Depends(get_db)):
    """Gets multiple enterprises starting from offset ends on limit"""
    enterprises = read_all(db, offset, limit)
    if enterprises and len(enterprises) > 0:
        return enterprises
    else:
        raise RuntimeError("Couldn't get")


@router.put("/enterprises/{enterprise_id}", response_model=schemas.Enterprise)
def update_enterprise(enterprise_id: int, to_update: schemas.EnterpriseCreate, db: Session = Depends(get_db)):
    """Updates enterprise with given data"""
    return update_by_id(db, enterprise_id, to_update)


@router.delete("/enterprises/{enterprise_id}")  # no response
def delete_enterprise(enterprise_id: int, db: Session = Depends(get_db)):
    """Deletes enterprise by its Id"""
    return delete(db, enterprise_id)
