from Base import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Enterprise(Base):

    __tablename__ = "Enterprise"
    Id: Mapped[id] = mapped_column(Integer, primary_key=True)
    Number_Of_Workers: Mapped[int] = mapped_column(Integer, nullable=False)
    Name_Of_Enterprise: Mapped[str] = mapped_column(String(42), nullable=False)
    Activity_Type: Mapped[str] = mapped_column(String(42), nullable=False)
