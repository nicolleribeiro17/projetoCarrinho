from pydantic import BaseModel
class Endereco(BaseModel):
    rua: str
    cep: str
    cidade: str
    estado: str
