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
        return db_user


'''/# Deleta um usuário do banco de dados
def delete_administrador(db: Session, administrador_matricula: str):
    db_administrador = db.query(models.Administrador).filter(models.Administrador.matricula == administrador_matricula).first()
    if db_administrador:
        db.delete(db_administrador)
        db.commit()/'''


def get_tarefas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Tarefa).offset(skip).limit(limit).all()


# Cria uma tarefa associada a um usuário
def create_tarefas(db: Session, tarefa: schemas.TarefaCreate, user_id: int):
    db_tarefa = models.Tarefa(**tarefa.dict(), owner_id=user_id)

    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)

    return db_tarefa


def delete_tarefa(db: Session, tarefa_id: int):
    db_tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == tarefa_id).first()

    # Verifica se a tarefa existe
    if db_tarefa:
        db.delete(db_tarefa)
        db.commit()

        return db_tarefa

'''/
db: Session: Representa uma sessão de banco de dados. Essa sessão é utilizada para realiar operações como inserção, consulta e confirmação de transações no banco de dados.

item: schemas.ItemCreate:
É um objeto que representa os dados necessários para criar um novo item, seguindo o esquema ItemCreate (definido em schemas). Esse esquema provavelmente contém campos como title e description, que são os atributos necessários para o item.

user_id: int:
O ID do usuário ao qual o item será associado. Isso relaciona o item criado a um usuário específico, identificando o dono do item.

/'''