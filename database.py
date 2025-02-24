from sqlmodel import SQLModel, create_engine


DATABASE_URL = "sqlite:///comanda.db"
engine = create_engine(DATABASE_URL, echo=True)


def criar_tabelas():
    SQLModel.metadata.create_all(engine)