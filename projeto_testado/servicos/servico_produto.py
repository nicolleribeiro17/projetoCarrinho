from modelo.carrinho import CarrinhoDeCompras
from servidor.uteis import db_produtos, db_carrinhos, db_produto_carrinho
from modelo.produto import Produto

# =====================================
# Persistencia para usuário
# =====================================

# Função que cadastra um produto 
def cadastrar_produto(produto: Produto):
    db_produtos.append(
        {
        "nome": produto.nome,
        "descricao": produto.descricao,
        "preco": produto.preco,
        "sku": produto.sku,
        "quantidade": produto.quantidade
        })
    return db_produtos

# Função que lista os produtos cadastrados
def lista_produtos():
    return db_produtos

# Função que calcula o preço total da lista de produtos
def preco_total():
    soma_total = 0
    for item in db_produtos:
        if item["preco"]:
            soma_total = soma_total + item["preco"]
    return ("Soma total do carrinho: ", soma_total)

# Função que associa os produtos cadastrados em um carrinho pelo nome do carrinho 
def cadastrar_produto_carrinho(carrinho: CarrinhoDeCompras):
    for elem in db_carrinhos:
        if elem.get("nome") == carrinho.nome:
            db_produto_carrinho.append({
                "carrinho": elem,
                "produtos": db_produtos
            })
    return db_produto_carrinho

# Função que retorna o carrinho com os produtos cadastrados 
def lista_carrinho_produto():
    return db_produto_carrinho

# Função que remove o produto da lista de produtos pelo sku
def remover_produto_cod(sku):
    for i, elem in enumerate(db_produtos):
        if elem.get("sku") == sku:
            db_produtos.pop(i)
    
    return db_produtos