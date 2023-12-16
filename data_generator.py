from Tables.enterprise import Enterprise
from Tables.products import Products
from Tables.shipments import Shipments
from faker import Faker
import random

fake = Faker()
fake_units_of_measurement = ['kg', 'cm', 'L', 'm', 'unit', 'g', 'mm', 'oz', 'lb']
fake_product_names = [
    "Quantum Chronicles: The Enigma",
    "Gizmo Prodigy's Handbook",
    "TechMaster's Journey: A Tale of Innovation",
    "The SuperFlex Throne: Epic Seating Saga",
    "EcoSmart Alchemy: Blending for a Greener Tomorrow",
    "Chronicles of Time: The Quantum Watch",
    "Lunar Odyssey Kit: Explore the Celestial",
    "Galactic Snackology: A Culinary Adventure",
    "Infinite Socks Chronicles",
    "Zenith Coffee Elegance: Brews and Beans",
    "Fusion Power Odyssey: Beyond Batteries",
    "Stellar Reality: Virtual Realms Unveiled",
    "AquaGlow Serenity: Hydration Enlightenment",
    "Velocity Tales: A Runners' Epic",
    "Evergreen Chronicles: Plant Kingdom Secrets",
    "MegaDrive Legends: Gaming Odyssey",
    "Harmony Chronicles: Thermostat Harmony",
    "Solaris Lumina: Laptop of Radiance",
    "Skyline Sojourn: Backpacking Expeditions",
    "Luxe Velvet Chronicles: Pillow Parnassus",
    "Enchanted Bookshelf: Literary Wonder",
    "Epicurean Odyssey: Culinary Escapades",
    "Mystic Inkwell: Quill of Imagination",
    "Celestial Candlelight: Illuminating Elegance",
    "Whimsical Whisk: Culinary Wand",
    "Labyrinth of Aromas: Fragrance Symphony",
    "Harmony Harmony: Harmonious Melodies",
    "Vivid Canvas: Artistry Unleashed",
    "Celestial Dreamcatcher: Nightly Wonders",
]


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
        Full_Name=random.choice(fake_product_names),
        Purchase_Price=round(random.uniform(50, 4500), 2),  # Sale price is more expensive than purchase price
        Expiration_Date=fake.date_this_decade(),
        Unit_Of_Measurement=random.choice(fake_units_of_measurement)
    )
