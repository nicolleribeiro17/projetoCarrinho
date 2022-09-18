import uvicorn
from fastapi import FastAPI
from rotas import usuario, enderecos, produto, raiz, carrinho

app = FastAPI()

app.include_router(usuario.router)
app.include_router(enderecos.router)
app.include_router(produto.router)
app.include_router(raiz.router)
app.include_router(carrinho.router)

if __name__ == "__main__":
    uvicorn.run(app)