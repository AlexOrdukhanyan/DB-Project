from Base import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

class Enterprise(Base):

    __tablename__ = "Enterprise"
    Id: Mapped[id] = mapped_column(Integer, primary_key=True)
    Number_Of_Workers: Mapped[int] = mapped_column(Integer, nullable=False)
    Name_Of_Enterprise: Mapped[str] = mapped_column(String(42), nullable=False)
    Activity_Type: Mapped[str] = mapped_column(String(42), nullable=False)

    Shipments: Mapped[List["Shipments"]] = relationship()

    def __str__(self):
        return f"Enterprise(Id={self.Id}, Number_Of_Workers={self.Number_Of_Workers}, " \
               f"Name_Of_Enterprise={self.Name_Of_Enterprise}, Activity_Type={self.Activity_Type})"
