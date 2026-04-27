from fastapi import FastAPI

from app.core.database import create_db_and_tables
from app.producto.routers import router as producto_router
from app.categoria.routers import router as categoria_router
from app.proveedores.routers import router as proveedores_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="API Integradora - Unidad 1",
        description="Conceptos: Path, Query, Body, Pydantic, Errores.",
        version="2.0.0",
    )

    app.include_router(producto_router)
    app.include_router(categoria_router)
    app.include_router(proveedores_router)

    @app.on_event("startup")
    def on_startup():
        create_db_and_tables()

    return app


app = create_app()