from data_generator import generate_product, generate_shipment, generate_enterprise
from typing import List, Any
import requests

BASE_URL = "http://localhost:8000"


def generate_shipments(amount: int = 3, product_id_range: tuple = (0, 2), enterprise_id_range: tuple = (0, 2)) -> List[Any]:
    return [generate_shipment(product_id_range, enterprise_id_range) for _ in range(amount)]


def generate_enterprises(amount: int = 3) -> List[Any]:
    return [generate_enterprise() for _ in range(amount)]


def generate_products(amount: int = 3) -> List[Any]:
    return [generate_product() for _ in range(amount)]


def populate_shipments(amount):
    data = generate_shipments(amount)
    requests.post(f"{BASE_URL}/shipments/", json=data)


def populate_products(amount):
    data = generate_products(amount)
    requests.post(f"{BASE_URL}/products/", json=data)


def populate_enterprises(amount):
    data = generate_enterprises(amount)
    serialized_data = [enterprise.to_dict() for enterprise in data]
    requests.post(f"{BASE_URL}/enterprises/", json=serialized_data)


"""def populate_products(amount):
    for _ in range(amount):
        data = generate_product()
        requests.post(f"{BASE_URL}/products/", json=data)


def populate_enterprises(amount):
    for _ in range(amount):
        data = generate_enterprise()
        data = data.to_dict()
        requests.post(f"{BASE_URL}/enterprises/", json=data)


def populate_shipments(amount):
    for _ in range(amount):
        data = generate_shipment()
        requests.post(f"{BASE_URL}/shipments/", json=data)
"""

if __name__ == "__main__":
    num_orders_to_create = 100
    populate_enterprises(num_orders_to_create)

    num_cars_to_create = 100
    populate_products(num_cars_to_create)

    num_auto_mechanics_to_create = 100
    populate_shipments(num_auto_mechanics_to_create)

    print('/Population completed/')
