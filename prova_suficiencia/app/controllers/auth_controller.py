from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.auth_schema import Token
from app.core.database import get_db
from app.core.security import get_usuario_autenticado, validar_senha, criar_token
from app.dao import usuario_dao

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    usuario = usuario_dao.buscar_por_email(db, form_data.username)

    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    if not validar_senha(form_data.password, usuario.senha):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token, expires_in = criar_token({"sub": usuario.email})

    return {"access_token": token, "token_type": "bearer", "expires_in": expires_in}


@router.post("/logout", status_code=200)
def logout(usuario=Depends(get_usuario_autenticado)):
    return {"message": f"Usuário {usuario.email} deslogado com sucesso"}
