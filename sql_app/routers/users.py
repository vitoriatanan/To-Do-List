from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sql_app import crud, schemas
from sql_app.database import get_db

# Criando um router específico para usuários
router = APIRouter()


# Cadastrando usuários. Verificando se já existe uma matrícula cadastrada
@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_matricula(db, matricula=user.matricula)
    if db_user:
        raise HTTPException(status_code=400, detail="Matrícula já cadastrada!")
    return crud.create_user(db=db, user=user)
    

# Deleta o usuário pela matrícula
@router.delete("/users/{user_matricula}", response_model=schemas.User)
def delete_user(user_matricula: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_matricula(db, matricula=user_matricula)
    if not db_user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    crud.delete_user(db, user_matricula=user_matricula)
    return db_user


