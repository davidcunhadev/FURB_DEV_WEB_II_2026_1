from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.models.comanda import comanda_produtos


from app.core.database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)

    comandas = relationship(
        "Comanda",
        secondary=comanda_produtos,
        back_populates="produtos",
    )
