from sqlalchemy.orm import Session
from app.dao import comanda_dao, produto_dao
from app.models.comanda import Comanda


def criar(db: Session, dados):
    produtos = []

    for p in dados["produtos"]:
        produto = produto_dao.buscar_por_id(db, p["id"])

        if not produto:
            raise ValueError(f"Produto {p['id']} não encontrado")

        produtos.append(produto)

    comanda = Comanda(
        id_cliente=dados["id_cliente"],
        nome_cliente=dados["nome_cliente"],
        telefone_cliente=dados["telefone_cliente"],
        produtos=produtos,
    )

    return comanda_dao.criar(db, comanda)


def listar(db: Session):
    return comanda_dao.listar(db)


def buscar_por_id(db: Session, comanda_id: int):
    comanda = comanda_dao.buscar_por_id(db, comanda_id)

    if not comanda:
        raise ValueError("Comanda não encontrada")

    return comanda


def atualizar(db: Session, comanda_id: int, dados):
    comanda = comanda_dao.buscar_por_id(db, comanda_id)

    if not comanda:
        raise ValueError("Comanda não encontrada")

    if "id_cliente" in dados:
        comanda.id_cliente = dados["id_cliente"]

    if "nome_cliente" in dados:
        comanda.nome_cliente = dados["nome_cliente"]

    if "telefone_cliente" in dados:
        comanda.telefone_cliente = dados["telefone_cliente"]

    if "produtos" in dados:
        produtos_existentes_ids = {p.id for p in comanda.produtos}

        for p in dados["produtos"]:
            produto = produto_dao.buscar_por_id(db, p["id"])

            if not produto:
                raise ValueError(f"Produto {p['id']} não encontrado")

            if produto.id not in produtos_existentes_ids:
                comanda.produtos.append(produto)

    return comanda_dao.atualizar(db, comanda)


def deletar(db: Session, comanda_id: int):
    comanda = comanda_dao.buscar_por_id(db, comanda_id)

    if not comanda:
        raise ValueError("Comanda não encontrada")

    comanda_dao.deletar(db, comanda)
