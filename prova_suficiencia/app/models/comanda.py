from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


comanda_produtos = Table(
    "comanda_produtos",
    Base.metadata,
    Column("comanda_id", ForeignKey("comandas.id"), primary_key=True),
    Column("produto_id", ForeignKey("produtos.id"), primary_key=True),
)


class Comanda(Base):
    __tablename__ = "comandas"

    id = Column(Integer, primary_key=True, index=True)
    id_cliente = Column(Integer, nullable=False)
    nome_cliente = Column(String(100), nullable=False)
    telefone_cliente = Column(String(20), nullable=False)

    produtos = relationship(
        "Produto",
        secondary=comanda_produtos,
        lazy="joined",
    )
