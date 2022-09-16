from pydantic import BaseModel

MEMORIA_CARRINHO = []
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

def persistencia_soma_total():
    soma_total = 0
    for item in MEMORIA_CARRINHO:
            if item['preco']:
                soma_total = soma_total + item['preco']
    return ("Soma total do carrinho:", soma_total)

def persistencia_deletar_produto_pelo_codigo(codigo):
    produto_deletar = None
    for i, item in enumerate(MEMORIA_CARRINHO):
        if item["codigo"] == codigo:
            produto_deletar = item
            MEMORIA_CARRINHO.pop(i)
            break
    return produto_deletar


# Classe representando os dados do produto
class Produto(BaseModel):
    nome: str
    descricao: str
    preco: float

# Classe representando o carrinho de compras de um cliente com uma lista de produtos
class Carrinho(BaseModel):
    id_usuario: int
    id_produto: list[Produto] = []
    preco_total: float
    quantidade_produtos: int