from data_generator import generate_product, generate_shipment, generate_enterprise
from typing import List, Any


def generate_shipments(amount: int) -> List[Any]:
    return [generate_shipment() for _ in range(amount)]


def generate_enterprises(amount: int) -> List[Any]:
    return [generate_enterprise() for _ in range(amount)]


def generate_products(amount: int) -> List[Any]:
    return [generate_product() for _ in range(amount)]
