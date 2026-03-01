from app.config import Config
from fastapi import FastAPI

from app.controllers import auth_controller, comanda_controller, produto_controller, usuario_controller
from app.core.database import Base, conexao
from app.models import usuario
from app.models import comanda
from app.models import produto


BASE_PREFIX = "/FurbWeb/v1"

app = FastAPI(title=Config.APP_NAME, docs_url=f"{BASE_PREFIX}/docs")

Base.metadata.create_all(bind=conexao)


@app.get(f"{BASE_PREFIX}/")
def start():
    return {
        "message": "API funcionando ;D"
    }


app.include_router(auth_controller.router, prefix=BASE_PREFIX)
app.include_router(usuario_controller.router, prefix=BASE_PREFIX)
app.include_router(produto_controller.router, prefix=BASE_PREFIX)
app.include_router(comanda_controller.router, prefix=BASE_PREFIX)
