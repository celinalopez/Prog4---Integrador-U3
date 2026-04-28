from sqlmodel import Session, select

from app.categoria.model import Categoria
from app.categoria.schema import CategoriaCreate


def create_categoria(session: Session, data: CategoriaCreate) -> Categoria:
    categoria = Categoria.model_validate(data)
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria


def get_categorias(session: Session, skip: int = 0, limit: int = 100) -> list[Categoria]:
    return session.exec(select(Categoria).offset(skip).limit(limit)).all()


def get_categoria_by_id(session: Session, categoria_id: int) -> Categoria | None:
    return session.get(Categoria, categoria_id)


def update_categoria(session: Session, categoria_id: int, data: CategoriaCreate) -> Categoria | None:
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        return None

    categoria.nombre = data.nombre
    categoria.descripcion = data.descripcion
    session.add(categoria)
    session.commit()
    session.refresh(categoria)
    return categoria


def delete_categoria(session: Session, categoria_id: int) -> bool:
    categoria = session.get(Categoria, categoria_id)
    if not categoria:
        return False

    session.delete(categoria)
    session.commit()
    return True
