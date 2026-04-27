from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ProductoBase(BaseModel):
    nombre: str = Field(..., examples=["Silla de Oficina"])
    categoria: str = Field(..., pattern=r"^[A-Z]{3}-\d{2}$", examples=["MUE-01"])
    precio: float = Field(..., gt=0, examples=[150.50])
    stock: int = Field(..., ge=0, examples=[20])
    stock_minimo: int = Field(..., ge=0, examples=[5])
    activo: bool = True


class ProductoCreate(ProductoBase):
    pass


class ProductoUpdate(BaseModel):
    nombre: Optional[str] = None
    categoria: Optional[str] = Field(None, pattern=r"^[A-Z]{3}-\d{2}$")
    precio: Optional[float] = Field(None, gt=0)
    stock: Optional[int] = Field(None, ge=0)
    stock_minimo: Optional[int] = Field(None, ge=0)
    activo: Optional[bool] = None


class ProductoRead(ProductoBase):
    model_config = ConfigDict(from_attributes=True)

    id: int


class ProductoStockResponse(BaseModel):
    stock: int
    bajo_stock_minimo: bool
    activo: bool