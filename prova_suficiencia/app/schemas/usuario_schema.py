from pydantic import BaseModel, EmailStr, Field


class UsuarioCreate(BaseModel):
    email: EmailStr
    senha: str = Field(
        min_length=6, max_length=72, description="Senha entre 6 e 72 caracteres"
    )


class UsuarioResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
