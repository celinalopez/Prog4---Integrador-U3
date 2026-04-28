from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.database import get_session
from app.categoria import schema, service

router = APIRouter(prefix="/categorias", tags=["Categorías"])


@router.post("/", response_model=schema.CategoriaRead, status_code=status.HTTP_201_CREATED)
def create_categoria(data: schema.CategoriaCreate, session: Session = Depends(get_session)):
    return service.create_categoria(session, data)


@router.get("/", response_model=List[schema.CategoriaRead])
def list_categorias(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return service.get_categorias(session, skip, limit)


@router.get("/{categoria_id}", response_model=schema.CategoriaRead)
def get_categoria(categoria_id: int, session: Session = Depends(get_session)):
    categoria = service.get_categoria_by_id(session, categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria


@router.put("/{categoria_id}", response_model=schema.CategoriaRead)
def update_categoria(
    categoria_id: int,
    data: schema.CategoriaUpdate,
    session: Session = Depends(get_session),
):
    categoria = service.update_categoria(session, categoria_id, data)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return categoria


@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_categoria(categoria_id: int, session: Session = Depends(get_session)):
    deleted = service.delete_categoria(session, categoria_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")