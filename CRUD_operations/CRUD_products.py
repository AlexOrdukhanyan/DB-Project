from sqlalchemy.orm import Session
from Tables.products import Products
from sqlalchemy import update
from schemas import ProductsCreate
from typing import List, Any


def create(db: Session, product: ProductsCreate) -> Products:
    """Creates product"""
    new_product = Products(
        Full_Name=product.Full_Name,
        Purchase_Price=product.Purchase_Price,
        Expiration_Date=product.Expiration_Date,
        Unit_Of_Measurement=product.Unit_Of_Measurement
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def read_one_by_id(db: Session, product_id: int) -> Products | None:
    """Returns product with given Id (Primary Key)"""
    return db.query(Products).get(product_id)


def read_one_by_name(db: Session, enterprise_name: str) -> Products | None:
    """Returns product with given name"""
    return db.query(Products).filter(Products.Full_Name == enterprise_name).first()


def read_all(db: Session, offset: int = 0, limit: int = 12) -> List[Any]:
    """Returns specific amount of values"""
    return db.query(Products).offset(offset).limit(limit).all()


def update_by_id(db: Session, product_id: int, new_product: ProductsCreate) -> Products:
    """Updates product with given Id with new_enterprise"""
    to_update = (
        update(Products).
        where(Products.Id == product_id).
        values(
            Full_Name=new_product.Full_Name,
            Purchase_Price=new_product.Purchase_Price,
            Expiration_Date=new_product.Expiration_Date,
            Unit_Of_Measurement=new_product.Unit_Of_Measurement
        )
    )
    db.execute(to_update)
    db.commit()

    return read_one_by_id(db, product_id)


def delete(db: Session, product_id: int) -> None:
    """Deletes a product with given Id"""
    db.delete(db.query(Products).get(product_id))
    db.commit()


def get_all(db: Session, per_page: int, page: int, _by: str) -> List[Products]:
    """Get all orders"""
    if _by == "Id" or _by == "id":
        obj = Products.Id
    elif _by == "name":
        obj = Products.Full_Name
    elif _by == "price":
        obj = Products.Purchase_Price
    elif _by == "date":
        obj = Products.Expiration_Date
    elif _by == "unit":
        obj = Products.Unit_Of_Measurement
    else:
        obj = Products.Id
    return (
        db.query(Products())
        .order_by(obj)
        .slice(page * per_page, page * per_page + per_page)
        .all()
    )
