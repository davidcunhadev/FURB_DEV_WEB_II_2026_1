from sqlalchemy.orm import Session
from app.dao import produto_dao


def criar(db: Session, dados: dict):
    return produto_dao.criar(db, dados)


def listar(db: Session):
    return produto_dao.listar(db)


def buscar_por_id(db: Session, produto_id: int):
    produto = produto_dao.buscar_por_id(db, produto_id)

    if not produto:
        raise ValueError("Produto não encontrado")

    return produto


def atualizar(db: Session, produto_id: int, dados: dict):
    produto = produto_dao.buscar_por_id(db, produto_id)

    if not produto:
        raise ValueError("Produto não encontrado")

    for key, value in dados.items():
        setattr(produto, key, value)

    return produto_dao.atualizar(db, produto)


def deletar(db: Session, produto_id: int):
    produto = produto_dao.buscar_por_id(db, produto_id)

    if not produto:
        raise ValueError("Produto não encontrado")

    produto_dao.deletar(db, produto)
