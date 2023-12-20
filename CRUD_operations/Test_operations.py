from sqlalchemy import func
from sqlalchemy.orm import Session
from sqlalchemy.sql import select
from Tables.shipments import Shipments
from Tables.products import Products
import datetime

from generators import generate_shipments, generate_products, generate_enterprises


def get_price_mean(db: Session) -> int:
    """Get mean of purchase prices"""
    data = db.query(func.round(func.avg(Products.Purchase_Price))).scalar()
    return data


def get_join_of_products_and_shipments(db: Session, per_page: int, page: int) -> list:
    """Get join of products and shipments"""
    data = (
        db.query(Products)
        .join(Shipments)
        .filter(Products.Id == Shipments.Products_Id)
        .order_by(Products.Id)
        .slice(page * per_page, page * per_page + per_page)
        .all()
    )
    result = []
    for product in data:
        result.append(
            {
                "Id": product.Id,
                "Full_Name": product.Full_Name,
                "Purchase_Price": product.Purchase_Price,
                "Expiration_Date": product.Expiration_Date,
                "Unit_Of_Measurement": product.Unit_Of_Measurement
            }
        )
    return result


def get_shipments_count_for_products(db: Session, per_page: int, page: int) -> list:
    """Get shipment count for products"""
    data = (
        db.query(Products, func.count(Products.Shipments).label("Shipment_Count"))
        .join(Shipments)
        .group_by(Products.Id)
        .slice(page * per_page, page * per_page + per_page)
    )
    result = []
    for product in data:
        result.append(
            {
                "Id": product[0].Id,
                "Full_name": product[0].Full_name,
                "Purchase_Price": product[0].Purchase_Price,
                "Expiration_Date": product[0].Expiration_Date,
                "Unit_Of_Measurement": product[0].Unit_Of_Measurement,
                "Shipment_Count": product[1],
            }
        )
    return result


def get_products_volume(db: Session, volume: int, per_page: int, page: int) -> list:
    """Get products with given volume or above"""
    subquery = (
        db.query(Shipments.Products_Id)
        .filter(Shipments.Volume_Of_Shipment >= volume)
        .subquery()
    )
    query = (
        db.query(Products)
        .filter(Products.Id.in_(select(subquery)))
        .slice(page * per_page, page * per_page + per_page)
    )
    result = []
    for product in query:
        result.append(
            {
                "Id": product.Id,
                "Full_Name": product.Full_Name,
                "Purchase_Price": product.Purchase_Price,
                "Expiration_Date": product.Expiration_Date,
                "Unit_Of_Measurement": product.Unit_Of_Measurement,
            }
        )
    return result


def update_price(db: Session, new_price: float, exp_date: datetime) -> None:
    """Update sale price, where expiration date is bigger, than given"""
    subquery = (
        db.query(Shipments.Id)
        .filter(Products.Expiration_Date <= exp_date)
        .subquery()
    )
    db.query(Shipments).filter(Shipments.Id.in_(select(subquery))).update(
        {"Sale_Price": new_price}
    )
    db.commit()


def generate_products_amount(db: Session, amount: int) -> str:
    """Generate products by given amount"""
    data = generate_products(amount)
    db.add_all(data)
    db.commit()
    return "Successfully created products"


def generate_enterprises_amount(db: Session, amount: int) -> str:
    """Generate enterprises by given amount"""
    data = generate_enterprises(amount)
    db.add_all(data)
    db.commit()
    return "Successfully created enterprises"


def generate_shipments_amount(db: Session, amount: int, product_id_range: tuple, enterprise_id_range: tuple) -> str:
    """Generate some shipments by given amount"""
    data = generate_shipments(amount, product_id_range, enterprise_id_range)
    db.add_all(data)
    db.commit()
    return "Successfully created shipments"
