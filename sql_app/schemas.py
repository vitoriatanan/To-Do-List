from pydantic import BaseModel


class TarefaBase(BaseModel):
    description: str

class TarefaCreate(TarefaBase):
    pass

class Tarefa(TarefaBase):
    id: int # Identifica unicamente a tarefa
    owner_id: int #Faz referência ao ID do usuário dono da tarefa

    class Config:
        orm_mode = True


# Molde para compartilhar campos comuns entre Usuário e Administrador
class UserBase(BaseModel):
    nome: str
    matricula: str


class UserCreate(UserBase):
    password: str
    is_adm: bool = False

class User(UserBase):
    id: int # Gerado automaticamete pelo banco de dados
    tarefas: list[Tarefa] = [] # Lista de objetos do tipo Tarefa, que são as tarefas associadas ao usuário
   
    class Config:
        orm_mode = True