from sqlalchemy.orm import Session, joinedload
from app.models.comanda import Comanda


def criar(db: Session, comanda: Comanda):
    db.add(comanda)
    db.commit()
    db.refresh(comanda)
    return comanda


def listar(db: Session):
    return db.query(Comanda).all()


def buscar_por_id(db: Session, comanda_id: int):
    return (
        db.query(Comanda)
        .options(joinedload(Comanda.produtos))
        .filter(Comanda.id == comanda_id)
        .first()
    )


def atualizar(db: Session, comanda: Comanda):
    db.commit()
    db.refresh(comanda)
    return comanda


def deletar(db: Session, comanda: Comanda):
    db.delete(comanda)
    db.commit()
