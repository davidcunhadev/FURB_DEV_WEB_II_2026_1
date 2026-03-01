from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str
    expires_in: int


class LoginData(BaseModel):
    email: EmailStr
    senha: str
