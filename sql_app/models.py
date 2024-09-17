# MODELOS DE BANCO DE DADOS
# modelos SQLAlchemy a partir da classe Base

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from .database import Base


# Column: serve para definir os campos(colunas) de uma tabela no banco de dados. Cada instancia de column descreve uma coluna individual de uma tabela, incluindo o tipo de dado que ela vai armazenar (Integer, String, Boolean)


#modelo sqlalchemy
class User(Base):
    __tablename__ = "users" #informa o nome da tabela a ser usada no banco de dados para cada um desses modelos

    id = Column(Integer, primary_key=True)
    # ao utilizar o SQLAlchemy, é comum e recomendado incluir um identificador único (como uma coluna id) para cada tabela, pois facilita o gerenciamento de registros, criação de relações entre tabelas (como o uso de chaves estrangeiras) e outras operações de banco de dados.
    nome = Column(String, unique=True)
    matricula = Column(String, unique=True, index=True)
    #unique garante que a matrícula deve ser única. Garante que não possam existir dois registros com o mesmo valor de matrícula
    #index: cria um índice na coluna, para acelerar as buscas e filtragens. Se frequentement consulta usuários pela matrícula, é interessante criar um índice nessa coluna.
    password = Column(String)
    is_adm = Column(Boolean, default=False)

    tarefas = relationship("Tarefa", back_populates="owner") #relacionamento com a tabela tarefas
    


'''/class Administrador(Base):
    __tablename__ = "administrador"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    matricula = Column(String, unique=True, index=True)
    password = Column(String)/'''


class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True) 
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id")) # Chave estrangeira que referencia o 'id' da tabela 'users'

    owner = relationship("User", back_populates="tarefas") # Relacionamento com a tabela 'users'

'''/
RESUMINDO
UserBase é apenas um molde para compartilhar campos comuns e economizar código.
UserCreate é usada para receber e validar os dados quando um novo usuário é criado, incluindo a senha.
User é usada para retornar os dados do usuário após ele ser criado, sem expor a senha.
/'''