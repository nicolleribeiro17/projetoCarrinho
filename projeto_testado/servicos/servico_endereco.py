from servidor.uteis import db_end, db_end_usuarios, db_usuarios
from modelo.usuario import Usuario
from modelo.endereco import Endereco

# =====================================
# Persistencia para endereços
# =====================================

# Função que cadastra o endereço
def cadastrar_endereco(endereco: Endereco):
    db_end.append({
        "rua": endereco.rua,
        "cep": endereco.cep,
        "cidade": endereco.cidade,
        "estado": endereco.estado
    })
    
    return db_end

# Função que lista os endereços cadastrados 
def lista_enderecos():
    return db_end

# Função que associa os endereços cadastrados a um usuário 
def cadastrar_enderecos_usuario(usuario: Usuario):
    for elem in db_usuarios:
        if elem.get("email") == usuario.email:
            db_end_usuarios.append({
                "usuario": elem,
                "enderecos": db_end
            })        
    
    return db_end_usuarios

# Função que lista os endereços do usuário cadastrados 
def lista_enderecos_usuario():
    return db_end_usuarios

# Função que remove os endereços do usuário pelo id do usuário 
def remover_endereco_usuario(id_usuario):
    end_deletar = None
    for i, elemento in enumerate(db_end_usuarios):
        if elemento["usuario"]["id"] == id_usuario:
            end_deletar = elemento
            db_end_usuarios.pop(i)
            break
    #return end_deletar  
    return db_end_usuarios

