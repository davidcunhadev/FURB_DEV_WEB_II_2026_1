from sqlalchemy.orm import Session
from app.models.produto import Produto


def criar(db: Session, dados: dict):
    produto = Produto(**dados)

    db.add(produto)
    db.commit()
    db.refresh(produto)

    return produto


def listar(db: Session):
    return db.query(Produto).all()


def buscar_por_id(db: Session, produto_id: int):
    return db.query(Produto).filter(Produto.id == produto_id).first()


def atualizar(db: Session, produto: Produto):
    db.commit()
    db.refresh(produto)
    return produto


def deletar(db: Session, produto: Produto):
    db.delete(produto)
    db.commit()
