from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "postgresql+psycopg://postgres:admin@localhost:5432/integrador3_db"

engine = create_engine(
    DATABASE_URL,
    echo=True,
)

connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, echo=False, connect_args=connect_args)


def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session