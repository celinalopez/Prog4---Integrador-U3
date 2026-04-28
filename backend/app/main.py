from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import create_db_and_tables
from app.categoria.router import router as categoria_router
from app.producto.router import router as producto_router
from app.producto_categoria.router import router as producto_categoria_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="FastAPI Productos",
        description="API para gestionar categorías, productos y su relación.",
        version="1.0.0",
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(categoria_router)
    app.include_router(producto_router)
    app.include_router(producto_categoria_router)

    @app.on_event("startup")
    def on_startup() -> None:
        create_db_and_tables()

    return app


app = create_app()