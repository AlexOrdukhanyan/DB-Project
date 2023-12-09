from Base import Base
from sqlalchemy import DateTime, Integer, String, Float
import datetime
from sqlalchemy.orm import Mapped, mapped_column


class Products(Base):

    __tablename__ = "Products"
    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Full_Name: Mapped[str] = mapped_column(String(42), nullable=False)
    Purchase_Price: Mapped[int] = mapped_column(Float, nullable=False)
    Expiration_Date: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)  # what if it doesn't have it?
    Unit_Of_Measurement: Mapped[str] = mapped_column(String, nullable=False)
