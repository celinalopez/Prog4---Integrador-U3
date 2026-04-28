from sqlmodel import Session, select

from app.producto.model import Producto
from app.producto.schema import ProductoCreate


def create_producto(session: Session, data: ProductoCreate) -> Producto:
    producto = Producto.model_validate(data)
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def get_productos(session: Session, skip: int = 0, limit: int = 100) -> list[Producto]:
    return session.exec(select(Producto).offset(skip).limit(limit)).all()


def get_producto_by_id(session: Session, producto_id: int) -> Producto | None:
    return session.get(Producto, producto_id)


def update_producto(session: Session, producto_id: int, data: ProductoCreate) -> Producto | None:
    producto = session.get(Producto, producto_id)
    if not producto:
        return None

    producto.nombre = data.nombre
    producto.descripcion = data.descripcion
    producto.precio_base = data.precio_base
    producto.imagen_url = data.imagen_url
    producto.disponible = data.disponible
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def delete_producto(session: Session, producto_id: int) -> bool:
    producto = session.get(Producto, producto_id)
    if not producto:
        return False

    session.delete(producto)
    session.commit()
    return True