from pydantic import BaseModel
import datetime

# classes for shipments


class ShipmentsBase(BaseModel):
    """Shipment Base"""
    Date_Of_Shipment: datetime.date
    Volume_Of_Shipment: int
    Sale_Price: float


class ShipmentsCreate(ShipmentsBase):
    """Creating Schema (in CRUD)"""
    pass


class Shipments(ShipmentsBase):
    """Schema for Shipment"""
    Id: int

    class Config:
        """Configuration class"""
        from_attributes = True


# classes for products


class ProductsBase(BaseModel):
    Full_Name: str
    Purchase_Price: int
    Expiration_Date: datetime.date
    Unit_Of_Measurement: str


class ProductsCreate(ProductsBase):
    pass


class Products(ProductsBase):
    Id: int

    class Config:
        from_attributes = True

# classes for enterprise


class EnterpriseBase(BaseModel):
    Number_Of_Workers: int
    Name_Of_Enterprise: str
    Activity_Type: str


class EnterpriseCreate(EnterpriseBase):
    pass


class Enterprise(EnterpriseBase):
    Id: int

    class Config:
        from_attributes = True
