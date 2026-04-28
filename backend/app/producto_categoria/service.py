from sqlmodel import Session, select

from app.producto_categoria.model import ProductoCategoria
from app.producto_categoria.schema import ProductoCategoriaCreate


def create_link(session: Session, data: ProductoCategoriaCreate) -> ProductoCategoria:
    link = ProductoCategoria.model_validate(data)
    session.add(link)
    session.commit()
    session.refresh(link)
    return link


def list_links(session: Session) -> list[ProductoCategoria]:
    return session.exec(select(ProductoCategoria)).all()