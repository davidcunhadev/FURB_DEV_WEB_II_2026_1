from pydantic import BaseModel, Field
from typing import Optional, List


class ProdutoRef(BaseModel):
    id: int


class ComandaCreate(BaseModel):
    id_cliente: int
    nome_cliente: str
    telefone_cliente: str
    produtos: List[ProdutoRef]


class ComandaUpdate(BaseModel):
    id_cliente: Optional[int] = None
    nome_cliente: Optional[str] = None
    telefone_cliente: Optional[str] = None
    produtos: Optional[List[ProdutoRef]] = None


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float

    class Config:
        from_attributes = True


class ComandaResponse(BaseModel):
    id_cliente: int = Field(alias="idCliente")
    nome_cliente: str = Field(alias="nomeCliente")
    telefone_cliente: str = Field(alias="telefoneCliente")
    produtos: List[ProdutoResponse]

    class Config:
        from_attributes = True
        populate_by_name = True
