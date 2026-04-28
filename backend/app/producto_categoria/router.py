from typing import List

from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.core.database import get_session
from app.producto_categoria import schema, service

router = APIRouter(prefix="/producto-categorias", tags=["ProductoCategoría"])


@router.post("/", response_model=schema.ProductoCategoriaRead, status_code=status.HTTP_201_CREATED)
def create_link(data: schema.ProductoCategoriaCreate, session: Session = Depends(get_session)):
    return service.create_link(session, data)


@router.get("/", response_model=List[schema.ProductoCategoriaRead])
def list_links(session: Session = Depends(get_session)):
    return service.list_links(session)