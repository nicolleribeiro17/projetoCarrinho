from servidor.uteis import db_usuarios
from modelo.usuario import Usuario


# =====================================
# Persistencia para usuário
# =====================================

# Função que cria o usuário
def criar_usuario(usuario: Usuario):
    id_usuario = 1
    obj_usuario = {
        "id": id_usuario
    }

    for elem in db_usuarios:
        if elem.get("id") == id_usuario:
            id_usuario += 1
            obj_usuario["id"] = id_usuario
          
    obj_usuario.update(
        {
            "nome": usuario.nome,
            "email": usuario.email
        }
    )
    
    novo_usuario = db_usuarios.append(obj_usuario)
    return db_usuarios

# Função que lista os usuários cadastrados
def lista_usuarios():
    return db_usuarios
    
# Função que retorna o usuário pelo id
def retornar_usuario_pelo_id(id):
    usuario_procurado = None
    for user in db_usuarios:
        if user["id"] == id:
            usuario_procurado = user
            break
    return usuario_procurado

# Função que retorna o usuário pelo primeiro nome
def retornar_usuario_pelo_nome(nome):
    nome_procurado = None
    for elem in db_usuarios:
        if elem["nome"].split(" ")[0] == nome:
            nome_procurado = elem
            break
    return nome_procurado

# Função que deleta o usuário
def deletar_usuario(id):
    usuario_deletar = None
    for i, user in enumerate(db_usuarios):
        if user["id"] == id:
            usuario_deletar = user
            db_usuarios.pop(i)
            break
    return db_usuarios
    #return usuario_deletar



            
    