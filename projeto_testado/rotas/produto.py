from fastapi import APIRouter
from modelo.carrinho import CarrinhoDeCompras
from modelo.produto import Produto
from servicos.servico_produto import cadastrar_produto,lista_produtos, cadastrar_produto_carrinho, preco_total, remover_produto_cod, lista_carrinho_produto

router = APIRouter(tags=['Produtos'], prefix="/produto")

@router.post("")
def adicionar_produto(produto: Produto):
    return cadastrar_produto(produto)

@router.get("")
def retorno_todos_produtos():
    produtos = lista_produtos()
    return produtos

@router.delete("")
def remover_produto_sku(sku):
    return remover_produto_cod(sku) 


@router.get("/total")
def soma_produtos():
    return preco_total()

@router.post("/carrinho")
def adicionar_produtos_carrinho(carrinho: CarrinhoDeCompras):
    return cadastrar_produto_carrinho(carrinho)

@router.get("/carrinho/")
def consultar_produtos_carrinho():
    lista = lista_carrinho_produto()
    return lista