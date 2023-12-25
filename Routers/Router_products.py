from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from typing import List

from database import get_db, SessionLocal
from CRUD_operations.CRUD_products import create, read_all, read_one_by_id, read_one_by_name, update_by_id, delete
import schemas

router = APIRouter()


@router.post("/products", response_model=schemas.Products)
def create_product(to_create: schemas.ProductsCreate, db: Session = Depends(get_db)):
    """Creates product with given data"""
    product = create(db, to_create)
    if product:
        return product
    else:
        raise RuntimeError("Couldn't create")


@router.get("/products/{product_id}", response_model=schemas.Products)
def get_product_by_id(product_id: int, db: Session = Depends(get_db)):
    """Gets product by id"""
    product = read_one_by_id(db, product_id)
    if product:
        return product
    else:
        raise RuntimeError("Couldn't get")


@router.get("/products/{product_name}", response_model=schemas.Products)
def get_product_by_name(product_name: str, db: Session = Depends(get_db)):
    """Gets product by name"""
    product = read_one_by_name(db, product_name)
    if product:
        return product
    else:
        raise RuntimeError("Couldn't get")


@router.get("/products", response_model=List[schemas.Products])
def get_multiple(offset: int = 0, limit: int = 12, db: Session = Depends(get_db)):
    """Gets multiple products starting from offset ends on limit"""
    products = read_all(db, offset, limit)
    if products and len(products) > 0:
        return products
    else:
        raise RuntimeError("Couldn't get")


@router.put("/products/{product_id}", response_model=schemas.Products)
def update_product(product_id: int, to_update: schemas.ProductsCreate, db: Session = Depends(get_db)):
    """Updates product with given data"""
    return update_by_id(db, product_id, to_update)


@router.delete("/products/{product_id}")  # no response
def delete_product(product_id: int, db: Session = Depends(SessionLocal)):
    """Deletes product by its Id"""
    return delete(db, product_id)
