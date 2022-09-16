
import fastapi
from endereco import persistencia_deletar_endereco_pelo_codigo
from endereco import persistencia_endereco_salvar
from endereco import persistencia_pesquisar_pelo_codigo_enderecos
from endereco import persistencia_endereco_pesquisar_todos
from usuario import persistencia_deletar_usuario_pelo_codigo
from usuario import persistencia_pesquisar_emails
from usuario import persistencia_pesquisar_pelo_codigo_usuario
from usuario import persistencia_pesquisar_pelo_nome_usuario
from usuario import persistencia_usuario_salvar
from usuario import persistencia_usuario_pesquisar_todos
from carrinho import persistencia_deletar_produto_pelo_codigo
from carrinho import persistencia_pesquisar_pelo_codigo_produto
from carrinho import persistencia_produto_salvar
from carrinho import persistencia_soma_total
from carrinho import persistencia_produto_pesquisar_todos
from endereco import Endereco
from carrinho import Carrinho
from carrinho import Produto
from usuario import Usuario

app = fastapi.FastAPI()



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
    print(f"Registrando um novo produto:", novo_produto.dict())
    novo_produto = persistencia_produto_salvar(novo_produto.dict())
    return novo_produto

# Rota que pesquisa e apresenta os produtos 
@app.get("/carrinho")
def rota_pesquisar_todos_produtos():
    carrinho = persistencia_produto_pesquisar_todos()
    return carrinho

# Rota que pesquisa e apresenta o produto pelo código 
@app.get("/carrinho/{codigo}")
def rota_pesquisar_produtos_pelo_codigo(codigo: int):
    print("Consulta pelo código", codigo)
    produto_encontrado = persistencia_pesquisar_pelo_codigo_produto(codigo)
    return produto_encontrado

# Rota que retorna a soma do carrinho
@app.get("/total")
def rota_soma_total_produtos():
    return persistencia_soma_total()
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
    usuarios = persistencia_usuario_pesquisar_todos()
    return usuarios

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
def rota_email_cadastrados():
    print("Consulta email")
    lista = persistencia_pesquisar_emails()
    return lista

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
def rota_cadastro_endereco(novo_endereco: Endereco):
    print(f"Registrando um novo endereço:", novo_endereco.dict())
    novo_endereco = persistencia_endereco_salvar(novo_endereco.dict())
    return novo_endereco

# Rota que pesquisa e apresenta os endereços 
@app.get("/enderecos")
def rota_pesquisar_todos_enderecos():
    end = persistencia_endereco_pesquisar_todos()
    return end

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