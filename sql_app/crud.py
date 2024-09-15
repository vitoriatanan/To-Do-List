from sqlalchemy.orm import Session

from . import models, schemas

# Leitura de um único usuário/administrador por ID
def get_user(db: Session, user_id: int, administrador_id: int):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    return user


# Leitura de um único usuário/administrador por matrícula
def get_user_by_matricula(db: Session, matricula: str):
    
    matricula_user = db.query(models.User).filter(models.User.matricula == matricula).first()
    return matricula_user 


# Leitura de vários usuários RETIRAR FUNCAAO
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Leitura de vários administradores RETIRAR FUNCAAAAAO
'''/def get_administradores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Administrador).offset(skip).limit(limit).all()/'''


# Criando usuários
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"     #TIRAR ESSE HASH
    db_user = models.User(nome=user.nome, matricula=user.matricula, password=fake_hashed_password, is_adm=user.is_adm)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



# Criando administradores
'''/def create_administrador(db: Session, administrador: schemas.AdministradorCreate):
    fake_hashed_password = administrador.password + "notreallyhashed" #TIRAR ESSE HASH
    db_administrador = models.Administrador(nome=administrador.nome, matricula=administrador.matricula, password=fake_hashed_password)
    db.add(db_administrador)
    db.commit()
    db.refresh(db_administrador)
    return db_administrador/'''



# Deleta um usuário do banco de dados
def delete_user(db: Session, user_matricula: str):
    db_user = db.query(models.User).filter(models.User.matricula == user_matricula).first()
    if db_user:
        db.delete(db_user)
        db.commit()


'''/# Deleta um usuário do banco de dados
def delete_administrador(db: Session, administrador_matricula: str):
    db_administrador = db.query(models.Administrador).filter(models.Administrador.matricula == administrador_matricula).first()
    if db_administrador:
        db.delete(db_administrador)
        db.commit()/'''


def get_tarefas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tarefa).offset(skip).limit(limit).all()

def create_tarefas(db: Session, item: schemas.TarefaCreate, user_id: int):
    db_tarefa = models.Tarefa(**tarefa.dict(), owner_id=user_id)
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    return db_tarefa