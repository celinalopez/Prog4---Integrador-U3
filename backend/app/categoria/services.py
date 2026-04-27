from sqlmodel import Session, select

from app.categoria.models import Categoria
from app.categoria.schemas import CategoriaCreate


def crear(session: Session, data: CategoriaCreate) -> Categoria:
    existente = session.exec(
        select(Categoria).where(Categoria.codigo == data.codigo)
    ).first()

    if existente:
        raise ValueError("Ya existe una categoría con ese código")

    nueva = Categoria.model_validate(data)
    session.add(nueva)
    session.commit()
    session.refresh(nueva)
    return nueva


def obtener_todas(session: Session, skip: int = 0, limit: int = 10) -> list[Categoria]:
    statement = select(Categoria).offset(skip).limit(limit)
    return session.exec(statement).all()


def obtener_por_id(session: Session, id: int) -> Categoria | None:
    return session.get(Categoria, id)


def actualizar_total(
    session: Session, id: int, data: CategoriaCreate
) -> Categoria | None:
    categoria = session.get(Categoria, id)
    if not categoria:
        return None

    existente = session.exec(
        select(Categoria).where(Categoria.codigo == data.codigo, Categoria.id != id)
    ).first()

    if existente:
        raise ValueError("Ya existe otra categoría con ese código")

    categoria.codigo = data.codigo
    categoria.descripcion = data.descripcion
    categoria.activo = data.activo

    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria


def desactivar(session: Session, id: int) -> Categoria | None:
    categoria = session.get(Categoria, id)
    if not categoria:
        return None

    categoria.activo = False
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria