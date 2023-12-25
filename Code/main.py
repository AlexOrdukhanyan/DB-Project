from fastapi import FastAPI
from database import engine, session
from Base import Base
from Routers.Router_enterprise import router as enterprise_router
from Routers.Router_products import router as product_router, delete_product
from Routers.Router_shipments import router as shipments_router
from Routers.Test_router import router as test_router
from Tables.products import Products
from datetime import datetime
from data_generator import generate_product, generate_shipment, generate_enterprise
from Routers.Test_router import update_sale_price
from Routers.Test_router import generate_products_by_amount

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    router=enterprise_router,
    prefix='/enterprises',
)

app.include_router(
    router=product_router,
    prefix='/products',
)

app.include_router(
    router=shipments_router,
    prefix='/shipments',
)

app.include_router(
    router=test_router,
    prefix='/test_router',
)

test_product = Products(
    Full_Name='Product to be proud of',
    Purchase_Price=1234.5,
    Expiration_Date=datetime.now(),
    Unit_Of_Measurement='pieces'
)
session.add(test_product)
session.commit()

test_product = Products(
    Full_Name='Lala',
    Purchase_Price=34.5,
    Expiration_Date=datetime.now(),
    Unit_Of_Measurement='grams'
)
session.add(test_product)
session.commit()


test_product = Products(
    Full_Name='Kamasutra',
    Purchase_Price=69.69,
    Expiration_Date=datetime.now(),
    Unit_Of_Measurement='pieces'
)
session.add(test_product)
session.commit()

products = session.query(Products).all()
for prod in products:
    print(prod)

product_to_upd = session.query(Products).filter_by(Full_Name='Kamasutra').first()
product_to_upd.Unit_Of_Measurement = 'Tonns'
session.commit()

products = session.query(Products).all()
for prod in products:
    print(prod)

product_to_del = session.query(Products).filter_by(Purchase_Price=69.69).first()
session.delete(product_to_del)
session.commit()

products = session.query(Products).all()
for prod in products:
    print(prod)

#delete_product(2)
#session.delete(get_product_by_id(2))
#session.commit()


#car_to_delete = session.query(Products).filter_by(Full_Name='Product to be proud of').first()
#session.delete(car_to_delete)
#session.commit()

"""pp = generate_shipment((1, 5), (2, 4))
print(pp)
prd = generate_products_by_amount(5, )
print(*prd)
"""