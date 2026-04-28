from typing import Optional

from sqlalchemy import Column, JSON
from sqlmodel import Field, SQLModel


class Producto(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True)
    descripcion: str
    precio_base: str
    imagen_url: list[str] = Field(default_factory=list, sa_column=Column(JSON))
    disponible: bool = True