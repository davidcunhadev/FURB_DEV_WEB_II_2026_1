from sqlalchemy.orm import Session

from app.core.security import hash_senha
from app.dao import usuario_dao


def criar_usuario(db: Session, email: str, senha: str):
    usuario_existente = usuario_dao.buscar_por_email(db, email)

    if usuario_existente:
        raise ValueError("Usuário já cadastrado")

    senha_hash = hash_senha(senha)
    return usuario_dao.criar_usuario(db, email, senha_hash)


def buscar_por_email(db: Session, email: str):
    usuario = usuario_dao.buscar_por_email(db, email)

    if usuario:
        return usuario
    else:
        raise ValueError("Usuário não encontrado")
