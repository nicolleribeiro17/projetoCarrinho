from pydantic import BaseModel

class Produto(BaseModel):
    nome: str
    descricao: str
    preco: float
    sku: str
    quantidade: int