from datetime import datetime, timedelta, timezone

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config import Config
from app.core.database import get_db
from app.dao import usuario_dao

oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")

SECRET_KEY = Config.SECRET_KEY
TEMPO_EXPIRACAO_MINUTOS_ACESSO_TOKEN = 60

password_hasher = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_senha(senha: str):
    return password_hasher.hash(senha)


def validar_senha(senha: str, senha_hash: str):
    return password_hasher.verify(senha, senha_hash)


def criar_token(data: dict):
    encode = data.copy()

    expires_delta = timedelta(
        minutes=TEMPO_EXPIRACAO_MINUTOS_ACESSO_TOKEN
    )

    expira_em = datetime.now(timezone.utc) + expires_delta

    encode["exp"] = expira_em

    token = jwt.encode(encode, SECRET_KEY, algorithm="HS256")

    return token, int(expires_delta.total_seconds())


def get_usuario_autenticado(
    token: str = Depends(oauth2), db: Session = Depends(get_db)
):
    erro_credenciais = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token Inválido",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        email: str = payload.get("sub")

        if email is None:
            raise erro_credenciais

    except JWTError:
        raise erro_credenciais

    usuario = usuario_dao.buscar_por_email(db, email)

    if usuario is None:
        raise erro_credenciais

    return usuario
