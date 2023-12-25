from Base import Base
from sqlalchemy import DateTime, Integer, String, Float
import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List


class Products(Base):

    __tablename__ = "Products"
    Id: Mapped[int] = mapped_column(Integer, primary_key=True)
    Full_Name: Mapped[str] = mapped_column(String(42), nullable=False)
    Purchase_Price: Mapped[float] = mapped_column(Float, nullable=False)
    Expiration_Date: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)  # what if it doesn't have it?
    Unit_Of_Measurement: Mapped[str] = mapped_column(String, nullable=False)

    Shipments: Mapped[List["Shipments"]] = relationship()

    def __str__(self):
        return f"Products(Id={self.Id}, Full_Name={self.Full_Name}, " \
               f"Purchase_Price={self.Purchase_Price}, Expiration_Date={self.Expiration_Date}, "\
               f"Unit_Of_Measurement={self.Unit_Of_Measurement})"
