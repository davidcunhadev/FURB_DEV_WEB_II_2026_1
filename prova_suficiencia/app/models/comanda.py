from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


comanda_produtos = Table(
    "comanda_produtos",
    Base.metadata,
    Column("comanda_id", Integer, ForeignKey("comandas.id")),
    Column("produto_id", Integer, ForeignKey("produtos.id")),
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
        back_populates="comandas",
    )
