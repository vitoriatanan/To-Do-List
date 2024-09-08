from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #SessionLocal é uma classe, ao criar uma instancia, será a sessão real do banco de dados 

Base = declarative_base() #retorna uma classe para criar os modelis ou classes de banco de dados (modelos ORM)
 