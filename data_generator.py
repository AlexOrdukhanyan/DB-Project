from Tables.enterprise import Enterprise
from Tables.products import Products
from Tables.shipments import Shipments
from faker import Faker
import random

fake = Faker()


def generate_shipment():
    return Shipments(
        Date_Of_Shipment=fake.date_this_decade(),
        Volume_Of_Shipment=fake.random_int(min=1, max=50),
        Sale_Price=round(random.uniform(100, 5500), 2)
    )


def generate_enterprise():
    return Enterprise(
        Number_Of_Workers=random.randint(15, 1200),
        Name_Of_Enterprise=fake.company(),
        Activity_Type=fake.job(),
    )


def generate_product():
    return Products(
        Full_Name=fake.name(),
        Purchase_Price=round(random.uniform(50, 4500), 2),  # Sale price is more expensive than purchase price
        Expiration_Date=fake.date_this_decade(),
        Unit_Of_Measurement=fake.unit_of_measurement()
    )
