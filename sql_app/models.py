# MODELOS DE BANCO DE DADOS
# modelos SQLAlchemy a partir da classe Base

from sqlalchemy import Column, ForeignKey, Integer, String

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
    

    # Relacionamento com a tabela Administrador
    administrador = relationship("Administrador", back_populates="owner")


class Administrador(Base):
    __tablename__ = "administrador"

    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    matricula = Column(String, unique=True, index=True)
    password = Column(String)

    #Chave estrangeira que referencia a tabela User
    owner_id = Column(Integer, ForeignKey("users.id")) 

    #Relacionamento com a tabela User
    owner = relationship("User", back_populates="administrador")