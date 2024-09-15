from fastapi import FastAPI
from sql_app.routers import users, administrador  # Importar os routers

from . import models
from .database import SessionLocal, engine


# Criação automática das tabelas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Incluindo o router de usuários
app.include_router(users.router, prefix="/api/v1")

# Incluindo o router de administradores
app.include_router(administrador.router, prefix="/api/v1")