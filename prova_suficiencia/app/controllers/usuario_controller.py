from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_usuario_autenticado
from app.schemas.usuario_schema import UsuarioCreate, UsuarioResponse
from app.services import usuario_service


router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.get("/me")
def usuario_logado(usuario=Depends(get_usuario_autenticado)):
    return {"id": usuario.id, "email": usuario.email}


@router.post("/", response_model=UsuarioResponse, status_code=201)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    try:
        novo_usuario = usuario_service.criar_usuario(db, usuario.email, usuario.senha)

        return novo_usuario
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{email}", response_model=UsuarioResponse, status_code=200)
def buscar_por_email(email: str, db: Session = Depends(get_db)):
    try:
        return usuario_service.buscar_por_email(db, email)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
