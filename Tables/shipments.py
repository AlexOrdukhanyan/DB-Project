from Base import Base
from sqlalchemy import DateTime, Integer, ForeignKey, Float
import datetime
from sqlalchemy.orm import Mapped, mapped_column


class Shipments(Base):

    __tablename__ = "Shipments"
    Id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    Date_Of_Shipment: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)
    Volume_Of_Shipment: Mapped[int] = mapped_column(Integer, nullable=False)
    Sale_Price: Mapped[float] = mapped_column(Float, nullable=False)  # price as float: hi to Ani

    Enterprise_Id: Mapped[int] = mapped_column(ForeignKey("Enterprise.Id"))
    Products_Id: Mapped[int] = mapped_column(ForeignKey("Products.Id"))

    def __str__(self):
        return f"Shipment(Id={self.Id}, Date_Of_Shipment={self.Date_Of_Shipment}, " \
               f"Volume_Of_Shipment={self.Volume_Of_Shipment}, Sale_Price={self.Sale_Price})"
