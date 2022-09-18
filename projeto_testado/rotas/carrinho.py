from fastapi import APIRouter
from modelo.carrinho import CarrinhoDeCompras
from servicos.servico_carrinho import criar_carrinho, retornar_carrinho_nome, deletar_carrinho, lista_carrinhos

router = APIRouter(tags=['Carrinhos'], prefix="/carrinho")

@router.post("")
def adiciona_carrinho(carrinho: CarrinhoDeCompras):
    return criar_carrinho(carrinho)

@router.get("")
def retorno_todos_carrinhos():
    carts = lista_carrinhos()
    return carts

@router.get("/{nome}")
def retorno_carrinho_pelo_nome(nome: str):
    cart = retornar_carrinho_nome(nome)
    return cart

@router.delete("/{nome}")
def remover_carrinho_pelo_nome(nome):
    return deletar_carrinho(nome)