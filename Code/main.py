from fastapi import FastAPI
from database import engine, get_db
from Base import Base
from Routers.Router_enterprise import router as enterprise_router
from Routers.Router_products import router as product_router
from Routers.Router_shipments import router as shipments_router
from data_generator import generate_product, generate_shipment, generate_enterprise
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
pp = generate_shipment((1, 5), (2, 4))
print(pp)
prd = generate_products_by_amount(5, )
print(*prd)
