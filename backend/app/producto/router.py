from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.core.database import get_session
from app.producto import schema, service

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post("/", response_model=schema.ProductoRead, status_code=status.HTTP_201_CREATED)
def create_producto(data: schema.ProductoCreate, session: Session = Depends(get_session)):
    return service.create_producto(session, data)


@router.get("/", response_model=List[schema.ProductoRead])
def list_productos(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    return service.get_productos(session, skip, limit)


@router.get("/{producto_id}", response_model=schema.ProductoRead)
def get_producto(producto_id: int, session: Session = Depends(get_session)):
    producto = service.get_producto_by_id(session, producto_id)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.put("/{producto_id}", response_model=schema.ProductoRead)
def update_producto(
    producto_id: int,
    data: schema.ProductoUpdate,
    session: Session = Depends(get_session),
):
    producto = service.update_producto(session, producto_id, data)
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return producto


@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_producto(producto_id: int, session: Session = Depends(get_session)):
    deleted = service.delete_producto(session, producto_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Producto no encontrado")