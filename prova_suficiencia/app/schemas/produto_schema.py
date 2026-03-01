from pydantic import BaseModel, Field


class ProdutoBase(BaseModel):
    nome: str = Field(min_length=2, max_length=100)
    preco: float = Field(gt=0)


class ProdutoCreate(BaseModel):
    nome: str = Field(min_length=2, max_length=100)
    preco: float = Field(gt=0)


class ProdutoResponse(ProdutoBase):
    id: int

    class Config:
        from_attributes = True
