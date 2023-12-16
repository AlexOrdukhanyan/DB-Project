from sqlalchemy.orm import Session
from Tables.enterprise import Enterprise
from sqlalchemy import update
from schemas import EnterpriseCreate
from typing import List, Any


def create(db: Session, enterprise: EnterpriseCreate) -> Enterprise:
    """Creates enterprise"""
    new_enterprise = Enterprise(
        Number_Of_Workers=enterprise.Number_Of_Workers,
        Name_Of_Enterprise=enterprise.Name_Of_Enterprise,
        Activity_Type=enterprise.Activity_Type
    )
    db.add(new_enterprise)
    db.commit()
    db.refresh(new_enterprise)
    return new_enterprise


def read_one_by_id(db: Session, enterprise_id: int) -> Enterprise | None:
    """Returns enterprise with given Id (Primary Key)"""
    return db.query(Enterprise).get(enterprise_id)


def read_one_by_name(db: Session, enterprise_name: str) -> Enterprise | None:
    """Returns enterprise with given name"""
    return db.query(Enterprise).filter(Enterprise.Name_Of_Enterprise == enterprise_name).first()


def read_all(db: Session, offset: int = 0, limit: int = 12) -> List[Any]:
    """Returns specific amount of values"""
    return db.query(Enterprise).offset(offset).limit(limit).all()


def update_by_id(db: Session, enterprise_id: int, new_enterprise: EnterpriseCreate) -> Enterprise:
    """Updates enterprise with given Id with new_enterprise"""
    to_update = (
        update(Enterprise).
        where(Enterprise.Id == enterprise_id).
        values(
            Number_Of_Workers=new_enterprise.Number_Of_Workers,
            Name_Of_Enterprise=new_enterprise.Name_Of_Enterprise,
            Activity_Type=new_enterprise.Activity_Type
        )
    )
    db.execute(to_update)
    db.commit()

    return read_one_by_id(db, enterprise_id)


def delete(db: Session, enterprise_id: int) -> None:
    """Deletes an enterprise with given Id"""
    db.delete(db.query(Enterprise).get(enterprise_id))
    db.commit()
