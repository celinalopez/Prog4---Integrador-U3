from sqlmodel import Field, SQLModel


class ProductoCategoria(SQLModel, table=True):
    producto_id: int = Field(primary_key=True, foreign_key="producto.id")
    categoria_id: int = Field(primary_key=True, foreign_key="categoria.id")