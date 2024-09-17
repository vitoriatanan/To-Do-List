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


# Criando tarefas para os usuários
@router.post("/users/{user_id}/tarefas/", response_model=schemas.Tarefa)
def create_tarefa_user(user_id: int, tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    return crud.create_tarefas(db=db, tarefa=tarefa, user_id=user_id)

# Deletar tarefas
@router.delete("/users/{tarefa_id}/tarefas/", response_model=schemas.Tarefa)
def delete_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    return crud.delete_tarefa(db=db, tarefa_id=tarefa_id)