from sqlalchemy.orm import Session

from . import models, schemas

# Leitura de um único usuário/administrador por ID
def get_user(db: Session, user_id: int, administrador_id: int):
    # Busca para encontrar o usuário 
    user = db.query(models.User).filter(models.User.id == user_id).first()

    # Se não encontrar o usuário, tenta encontrar o administrador
    if not user:
       return db.query(models.Administrador).filter(models.Administrador.id == administrador_id).first()
    
    return user

# Leitura de um único usuário/administrador por matrícula
def get_user_by_matricula(db: Session, matricula: str):
    matricula_user = db.query(models.User).filter(models.User.matricula == matricula).first()

    if not matricula:
        return db.query(models.Administrador).filter(models.Administrador.matricula == matricula).first()
    
    return matricula_user

# Leitura de vários usuários
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

# Leitura de vários administradores
def get_administradores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Administrador).offset(skip).limit(limit).all()



def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(nome=user.nome, matricula=user.matricula, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user



def create_administrador(db: Session, administrador: schemas.AdministradorCreate, administrador_id: int):
    fake_hashed_password = administrador.password + "notreallyhashed"
    db_administrador = models.Administrador(nome=administrador.nome, matricula=administrador.matricula, password=fake_hashed_password, owner_id=user_id)
    db.add(db_administrador)
    db.commit()
    db.refresh(db_administrador)
    return db_administrador