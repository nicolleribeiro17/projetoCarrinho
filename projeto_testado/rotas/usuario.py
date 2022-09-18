from fastapi import APIRouter
from modelo.usuario import Usuario
from servicos.servico_usuario import criar_usuario, retornar_usuario_pelo_id, retornar_usuario_pelo_nome, deletar_usuario, lista_usuarios

router = APIRouter(tags=['Usuarios'], prefix="/usuario")

@router.post("")
def adicionar_usuario(usuario: Usuario):
    return criar_usuario(usuario)

@router.get("")
def pesquisa_todos_usuarios():
    usuarios = lista_usuarios()
    return usuarios

@router.get("/{id}")
def retorno_usuario(id: int):
    usuario = retornar_usuario_pelo_id(id)
    return usuario

@router.get("/nome/{nome}")
def retorno_usuario_com_nome(nome):
    return retornar_usuario_pelo_nome(nome)


@router.delete("/{id}")
def rota_deletar_usuario_pelo_id(id):
    return deletar_usuario(id)
    