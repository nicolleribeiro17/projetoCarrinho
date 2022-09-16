
from pydantic import BaseModel

MEMORIA_USUARIO = []

# =====================================
# Persistencia para usuário
# =====================================
def persistencia_usuario_salvar(novo_usuario):
    id_novo_usuario = len(MEMORIA_USUARIO) + 1
    novo_usuario["id"] = id_novo_usuario
    MEMORIA_USUARIO.append(novo_usuario)
    return novo_usuario

def persistencia_usuario_pesquisar_todos():
    lista_usuarios = list(MEMORIA_USUARIO)
    return lista_usuarios

def persistencia_pesquisar_pelo_codigo_usuario(id):
    usuario_procurado = None
    for usuario in MEMORIA_USUARIO:
        if usuario["id"] == id:
            usuario_procurado = usuario
            break
    return usuario_procurado

def persistencia_pesquisar_pelo_nome_usuario(nome):
    nome_procurado = None
    for i in MEMORIA_USUARIO:
        if i["nome"] == nome:
            nome_procurado = i
            break
    return nome_procurado

def persistencia_pesquisar_emails(email):
    lista_email = []
    for i in MEMORIA_USUARIO:
        if i["email"] == email:
            lista_email.append(i)
    return lista_email

def persistencia_deletar_usuario_pelo_codigo(id):
    usuario_deletar = None
    for i, usuario in enumerate(MEMORIA_USUARIO):
        if usuario["id"] == id:
            usuario_deletar = usuario
            MEMORIA_USUARIO.pop(i)
            break
    return usuario_deletar


# Classe representando os dados do cliente
class Usuario(BaseModel):
    nome: str
    email: str
    senha: str


