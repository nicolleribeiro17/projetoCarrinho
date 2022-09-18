from fastapi import APIRouter
from modelo.endereco import Endereco
from modelo.usuario import Usuario
from servicos.servico_endereco import cadastrar_endereco, cadastrar_enderecos_usuario, remover_endereco_usuario, lista_enderecos_usuario, lista_enderecos

router = APIRouter(tags=['Enderecos'], prefix="/endereco")

@router.post("")
def adicionar_endereco(endereco: Endereco):
    return cadastrar_endereco(endereco)

@router.post("/user")
def adicionar_endereco_usuario(usuario: Usuario):
    return cadastrar_enderecos_usuario(usuario)

@router.get("")
def pesquisar_enderecos_cadastrados():
    end_user = lista_enderecos()
    return end_user

@router.delete("/user/{id_usuario}")
def deletar_endereco_usuario(id_usuario):
    return remover_endereco_usuario(id_usuario)

@router.get("/user/")
def pesquisar_todos_enderecos_usuario():
    end = lista_enderecos_usuario()
    return end



