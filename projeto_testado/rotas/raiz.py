from fastapi import APIRouter

router = APIRouter(tags=['Verificação'])


# Rota Raiz 
@router.get("/")
def rota_raiz():
    site = "Seja bem vinda"
    return site.replace('\n', '')