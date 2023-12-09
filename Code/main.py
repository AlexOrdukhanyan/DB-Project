from sqlalchemy import create_engine
from database import engine
from Base import Base
import Tables.enterprise, Tables.products, Tables.shipments


Base.metadata.create_all(bind=engine)
