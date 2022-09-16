from pydantic import BaseModel

MEMORIA_ENDERECOS = []

# =================================
# Persistencia para endereço
# =================================
def persistencia_endereco_salvar(novo_endereco):
    CODIGO = len(MEMORIA_ENDERECOS) + 1
    novo_endereco["CODIGO"] = CODIGO
    MEMORIA_ENDERECOS.append(novo_endereco)
    return novo_endereco

def persistencia_endereco_pesquisar_todos():
    lista_enderecos = list(MEMORIA_ENDERECOS)
    return lista_enderecos

def persistencia_pesquisar_pelo_codigo_enderecos(CODIGO):
    endereco_procurado = None
    for endereco in MEMORIA_ENDERECOS:
        if endereco["CODIGO"] == CODIGO:
            endereco_procurado = endereco
            break
    return endereco_procurado

def persistencia_deletar_endereco_pelo_codigo(CODIGO):
    endereco_deletar = None
    for i, endereco in enumerate(MEMORIA_ENDERECOS):
        if endereco["CODIGO"] == CODIGO:
            endereco_deletar = endereco
            MEMORIA_ENDERECOS.pop(i)
            break
    return endereco_deletar

# Classe representando os dados do endereço do cliente
class Endereco(BaseModel):
    rua: str
    cep: str
    cidade: str
    estado: str