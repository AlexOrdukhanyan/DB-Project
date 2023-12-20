import datetime
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from database import get_db, SessionLocal
from CRUD_operations.Test_operations import (get_price_mean, get_products_volume,
                                             get_join_of_products_and_shipments, generate_products_amount,
                                             generate_shipments_amount, generate_enterprises_amount,
                                             get_shipments_count_for_products, update_price, group_sort_by_unit)

router = APIRouter()


@router.get("/products/mean", response_model=int)
def get_purchase_price_mean(db: Session = Depends(SessionLocal)):
    """Get mean of the purchase price"""
    res = get_price_mean(db)
    if res:
        return res
    else:
        raise RuntimeError("Couldn't get")


@router.get("/shipments/count", response_model=list)
def get_shipments_count(per_page: int = 10, page: int = 0, db: Session = Depends(SessionLocal)):
    """Get shipments count"""
    res = get_shipments_count_for_products(db, per_page, page)
    if res:
        return res
    else:
        raise RuntimeError("Couldn't get")


@router.get("/products/shipments", response_model=list)
def get_join(per_page: int = 10, page: int = 0, db: Session = Depends(SessionLocal)):
    """Get join of products and shipments"""
    res = get_join_of_products_and_shipments(db, per_page, page)
    if res:
        return res
    else:
        raise RuntimeError("Couldn't join")


@router.get("/products/shipments/volume", response_model=list)
def get_products_with_volume(volume: int, per_page: int = 10,page: int = 0, db: Session = Depends(SessionLocal)):
    """Get products with given volume or above"""
    res = get_products_volume(db, volume, per_page, page)
    if res:
        return res
    else:
        raise RuntimeError("Couldn't get")


@router.get("/products/group_unit", response_model=list)
def get_grouped_sorted_by_unit(per_page: int = 10, page: int = 0, db: Session = Depends(SessionLocal)):
    """Get grouping and sorting by unit of measurement"""
    res = group_sort_by_unit(db, per_page, page)
    if res:
        return res
    else:
        raise RuntimeError("Couldn't get")


@router.put('/auto_mechanics/update_planned_end_date', response_model=str)
def update_sale_price(new_price: float, exp_date: datetime, db: Session = Depends(SessionLocal)):
    """Update sale price, where expiration date is bigger, than given"""
    update_price(db, new_price, exp_date)
    return "Successfully updated"


@router.post('/products/generate', response_model=str)
def generate_products_by_amount(amount: int, db: Session = Depends(SessionLocal)):
    """Generate products by some amount"""
    return generate_products_amount(db, amount)


@router.post('/enterprises/generate', response_model=str)
def generate_enterprises_by_amount(amount: int, db: Session = Depends(SessionLocal)):
    """Generate enterprises by some amount"""
    return generate_enterprises_amount(db, amount)


@router.post('/shipments/generate', response_model=str)
def generate_shipments_by_amount(quantity: int, product_id_start: int, product_id_end: int,
                                 enterprise_id_start: int, enterprise_id_end: int, db: Session = Depends(SessionLocal),
                                 ):
    """Generate shipments by some amount"""
    return generate_shipments_amount(db, quantity, (product_id_start, product_id_end),
                                     (enterprise_id_start, enterprise_id_end),
                                     )
