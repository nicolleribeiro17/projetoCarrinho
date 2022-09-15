import fastapi
import pydantic 
from typing import Optional

app = fastapi.FastAPI()

# Persistência / Repositório
MEMORIA_CARRINHO = []
MEMORIA_USUARIO = []
MEMORIA_ENDERECOS = []

# =================================
# Persistencia para produto
# =================================
def persistencia_produto_salvar(novo_produto):
    codigo_novo_produto = len(MEMORIA_CARRINHO) + 1
    novo_produto["codigo"] = codigo_novo_produto
    MEMORIA_CARRINHO.append(novo_produto)
    return novo_produto

def persistencia_produto_pesquisar_todos():
    lista_produtos = list(MEMORIA_CARRINHO)
    return lista_produtos

def persistencia_pesquisar_pelo_codigo_produto(codigo):
    produto_procurado = None
    for item in MEMORIA_CARRINHO:
        if item["codigo"] == codigo:
            produto_procurado = item
            break
    return produto_procurado

def persistencia_soma_total(preco):
    soma_total = None
    for preco in MEMORIA_CARRINHO:
        soma_total = soma_total + preco
    return soma_total

def persistencia_deletar_produto_pelo_codigo(codigo):
    produto_deletar = None
    for i, item in enumerate(MEMORIA_CARRINHO):
        if item["codigo"] == codigo:
            produto_deletar = item
            MEMORIA_CARRINHO.pop(i)
            break
    return produto_deletar

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
    lista_email = None
    for i in MEMORIA_USUARIO:
        if i["email"] == email:
            lista_email.append(i)
    return lista_email

def persistencia_deletar_usuario_pelo_codigo(id):
    usuario_deletar = None
    for i, usuario in enumerate(MEMORIA_USUARIO):
        if usuario["id"] == id:
            usuarip_deletar = usuario
            MEMORIA_USUARIO.pop(i)
            break
    return usuario_deletar

# =================================
# Persistencia para endereço
# =================================
def persistencia_endereco_salvar(novo_endereco):
    CODIGO = len(MEMORIA_ENDERECOS) + 1
    novo_endereco["CODIGO"] = CODIGO
    MEMORIA_ENDERECOS.append(novo_endereco)
    return novo_endereco

def persistencia_endereco_pesquisar_todos():
    lista_enderecos = list(MEMORIA_ENDERECOS)
    return lista_enderecos

def persistencia_pesquisar_pelo_codigo_enderecos(CODIGO):
    endereco_procurado = None
    for endereco in MEMORIA_ENDERECOS:
        if endereco["CODIGO"] == CODIGO:
            endereco_procurado = endereco
            break
    return endereco_procurado

def persistencia_deletar_endereco_pelo_codigo(CODIGO):
    endereco_deletar = None
    for i, endereco in enumerate(MEMORIA_ENDERECOS):
        if endereco["CODIGO"] == CODIGO:
            endereco_deletar = endereco
            MEMORIA_ENDERECOS.pop(i)
            break
    return endereco_deletar


# Classe representando os dados do produto
class Produto(pydantic.BaseModel):
    nome: str
    descricao: str
    preco: float

# Classe representando os dados do cliente
class Usuario(pydantic.BaseModel):
    nome: str
    email: str
    senha: str

# Classe representando os dados do endereço do cliente
class Enderecos(pydantic.BaseModel):
    rua: str
    cep: str
    cidade: str
    estado: str

# Classe representando o carrinho de compras de um cliente com uma lista de produtos
class Carrinho(pydantic.BaseModel):
    id_usuario: int
    id_produto: list[Produto] = []
    preco_total: float
    quantidade_produtos: int


# Rota Raiz 
@app.get("/")
def rota_raiz():
    site = "Seja bem vinda"
    return site.replace('\n', '')

# ==============================================
# Rota cadastro de produtos no carrinho 
# ==============================================

@app.post("/carrinho")
def rota_cadastro_produto(novo_produto: Produto):
    print(f"Registrando uma nova música:", novo_produto.dict())
    novo_produto = persistencia_produto_salvar(novo_produto.dict())
    return novo_produto

# Rota que pesquisa e apresenta os produtos 
@app.get("/carrinho")
def rota_pesquisar_todos_produtos():
    return MEMORIA_CARRINHO

# Rota que pesquisa e apresenta o produto pelo código 
@app.get("/carrinho/{codigo}")
def rota_pesquisar_produtos_pelo_codigo(codigo: int):
    print("Consulta pelo código", codigo)
    produto_encontrado = persistencia_pesquisar_pelo_codigo_produto(codigo)
    return produto_encontrado

# Rota que retorna a soma do carrinho
@app.get("carrinho/total")
def rota_soma_total_produtos(preco: float):
    soma_total = persistencia_soma_total(preco)
    return soma_total
    #return {"Soma_total": sum(preco)}

# Rota que deleta o produto pelo código
@app.delete("/carrinho/{codigo}")
def rota_deletar_produto_pelo_codigo(codigo: int):
    print("Consulta pelo código", codigo)
    produto_deletada = persistencia_deletar_produto_pelo_codigo(codigo)
    return produto_deletada

# =========================
# Rota cadastro usuário 
# =========================
@app.post("/usuarios")
def rota_cadastro_usuario(novo_usuario: Usuario):
    print(f"Registrando um novo usuário:", novo_usuario.dict())
    novo_usuario = persistencia_usuario_salvar(novo_usuario.dict())
    return novo_usuario

# Rota que pesquisa e apresenta os usuários 
@app.get("/usuarios")
def rota_pesquisar_todos_usuarios():
    return MEMORIA_USUARIO

# Rota que pesquisa e apresenta o produto pelo id
@app.get("/usuarios/{id}")
def rota_pesquisar_usuario_pelo_id(id: int):
    print("Consulta pelo código", id)
    usuario_encontrado = persistencia_pesquisar_pelo_codigo_usuario(id)
    return usuario_encontrado

# Rota que pesquisa e apresenta o usuário pelo nome 
@app.get("/usuarios/nome/{nome}")
def rota_pesquisar_usuario_pelo_nome(nome: str):
    print("Consulta pelo código", nome)
    nome_encontrado = persistencia_pesquisar_pelo_nome_usuario(nome)
    return nome_encontrado

# Rota que apresenta os emails cadastrados
@app.get("/usuarios/mail")
def rota_email_cadastrados(email: str):
    print("Consulta email", email)
    lista_email = persistencia_pesquisar_emails(email)
    return lista_email

# Rota que deleta o usuário pelo id
@app.delete("/usuarios/{id}")
def rota_deletar_usuario_pelo_id(id: int):
    print("Consulta pelo código", id)
    usuario_deletado = persistencia_deletar_usuario_pelo_codigo(id)
    return usuario_deletado

# =================================
#  ** Rota cadastro endereço ***
# =================================
@app.post("/enderecos")
def rota_cadastro_endereco(novo_endereco: Enderecos):
    print(f"Registrando um novo endereço:", novo_endereco.dict())
    novo_endereco = persistencia_endereco_salvar(novo_endereco.dict())
    return novo_endereco

# Rota que pesquisa e apresenta os endereços 
@app.get("/enderecos")
def rota_pesquisar_todos_enderecos():
    return MEMORIA_ENDERECOS

# Rota que pesquisa e apresenta o endereço pelo código 
@app.get("/enderecos/{CODIGO}")
def rota_pesquisar_endereco_pelo_codigo(CODIGO: int):
    print("Consulta pelo código", CODIGO)
    endereco_encontrado = persistencia_pesquisar_pelo_codigo_enderecos(CODIGO)
    return endereco_encontrado

# Rota que deleta o endereço pelo código
@app.delete("/enderecos/{CODIGO}")
def rota_deletar_endereco_pelo_codigo(CODIGO: int):
    print("Consulta pelo código", CODIGO)
    endereco_deletado = persistencia_deletar_endereco_pelo_codigo(CODIGO)
    return endereco_deletado