from pydantic import BaseModel


class TarefaBase(BaseModel):
    description: str

class TarefaCreate(TarefaBase):
    pass

class Tarefa(TarefaBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


#Por segurança a senha não estará nos modelos pydantic, não será enviafo pel api ao ler um usuário.

# classe Base definem os campos essenciais )atributos comuns) que todas as outras classes derivadas compartilham. São usadas para evitar repetição de código e para definir os atributos principais de Item e User

# Molde para compartilhar campos comuns entre Usuário e Administrador
class UserBase(BaseModel):
    nome: str
    matricula: str



# classes Create são usadas especcificamente para validação de entrada quando está criando novos objetos. Quando um novo usuário é criado, além do email, é necessário também o campo password, que não está em UserBase
#As classes ItemCreate e UserCreate são separadas porque, ao criar novos objetos, os dados esperados são diferentes dos dados retornados (por exemplo, id não é fornecido ao criar, mas é necessário ao retornar o objeto).
# Criação de usuário com senha
class UserCreate(UserBase):
    password: str
    is_adm: bool = False


# Representação de saída e para a conversão de objetos de banco de dados em objetos Pydantic (via orm_mode)
#Quando o usuário é retornado pela API, ele vem com id, nome, matricula
# Retorno de usuário sem senha
class User(UserBase):
    id: int #gerado automaticamete pelo banco de dados
    tarefas: list[Tarefa] = []
   
    class Config:
        orm_mode = True


'''/# Criação de administrador com senha
class AdministradorCreate(UserBase):
    password: str

# Retorno de administrador sem senha
class Administrador(UserBase):
    id: int

    class Config:
        orm_mode = True


RESUMINDO
UserBase é apenas um molde para compartilhar campos comuns e economizar código.
UserCreate é usada para receber e validar os dados quando um novo usuário é criado, incluindo a senha.
User é usada para retornar os dados do usuário após ele ser criado, sem expor a senha.
/'''