from sqlmodel import Session, select

from app.producto.models import Producto
from app.producto.schemas import ProductoCreate


def crear(session: Session, data: ProductoCreate) -> Producto:
    nuevo = Producto.model_validate(data)
    session.add(nuevo)
    session.commit()
    session.refresh(nuevo)
    return nuevo


def obtener_todos(session: Session, skip: int, limit: int) -> list[Producto]:
    statement = select(Producto).offset(skip).limit(limit)
    return session.exec(statement).all()


def obtener_por_id(session: Session, id: int) -> Producto | None:
    return session.get(Producto, id)


def actualizar_total(
    session: Session, id: int, data: ProductoCreate
) -> Producto | None:
    producto = session.get(Producto, id)
    if not producto:
        return None

    producto.nombre = data.nombre
    producto.categoria = data.categoria
    producto.precio = data.precio
    producto.stock = data.stock
    producto.stock_minimo = data.stock_minimo
    producto.activo = data.activo

    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def desactivar(session: Session, id: int) -> Producto | None:
    producto = session.get(Producto, id)
    if not producto:
        return None

    producto.activo = False
    session.add(producto)
    session.commit()
    session.refresh(producto)
    return producto


def obtener_estado_stock(session: Session, id: int) -> dict | None:
    producto = session.get(Producto, id)
    if not producto:
        return None

    alerta_stock = producto.stock < producto.stock_minimo

    return {
        "stock": producto.stock,
        "bajo_stock_minimo": alerta_stock,
        "activo": producto.activo,
    }