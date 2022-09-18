from servidor.uteis import db_carrinhos
from modelo.carrinho import CarrinhoDeCompras

# =====================================
# Persistencia para usuário
# =====================================

# Função que cadastra um carrinho 
def criar_carrinho(carrinho: CarrinhoDeCompras):
    id_carrinho = 1
    obj_carrinho = {
        "id": id_carrinho
    }
    for elem in db_carrinhos:
        if elem.get("id") == id_carrinho:
            id_carrinho += 1
            obj_carrinho["id"] =  id_carrinho

    obj_carrinho.update( 
        {
            "nome": carrinho.nome
        }
    )

    cart = db_carrinhos.append(obj_carrinho)
    return db_carrinhos

# Função que lista os carrinhos cadastrados
def lista_carrinhos():
    return db_carrinhos
    
# Função que retorna o carrinho pelo seu nome
def retornar_carrinho_nome(nome):
    carrinho_procurado = None
    for elem in db_carrinhos:
        if elem["nome"] == nome:
            carrinho_procurado = elem
            break       
    return carrinho_procurado
    
# Função que deleta o carrinho pelo seu nome
def deletar_carrinho(nome):
    carrinho_deletar = None
    for i, elem in enumerate(db_carrinhos):
        if elem.get("nome") == nome:
            carrinho_deletar = elem
            db_carrinhos.pop(i)
            break
    return db_carrinhos
