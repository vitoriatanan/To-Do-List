from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .database import Base


#modelo sqlalchemy
class User(Base):
    __tablename__ = "users" 
    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    matricula = Column(String, unique=True, index=True)
    password = Column(String)
    is_adm = Column(Boolean, default=False)

    tarefas = relationship("Tarefa", back_populates="owner") 


class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True) 
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id")) # Chave estrangeira que referencia o 'id' da tabela 'users'

    owner = relationship("User", back_populates="tarefas") # Relacionamento com a tabela 'users'
