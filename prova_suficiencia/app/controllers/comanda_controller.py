from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_usuario_autenticado
from app.schemas.comanda_schema import (
    ComandaCreate,
    ComandaResponse,
    ComandaUpdate,
)
from app.services import comanda_service

router = APIRouter(prefix="/comandas", tags=["Comandas"])


@router.post("/", response_model=ComandaResponse, status_code=201)
def criar(
    comanda: ComandaCreate,
    db: Session = Depends(get_db),
    user=Depends(get_usuario_autenticado),
):
    try:
        return comanda_service.criar(db, comanda.model_dump())
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.get("/", response_model=list[ComandaResponse])
def listar(
    db: Session = Depends(get_db),
    user=Depends(get_usuario_autenticado),
):
    return comanda_service.listar(db)


@router.get("/{comanda_id}", response_model=ComandaResponse)
def buscar_por_id(
    comanda_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_usuario_autenticado),
):
    try:
        return comanda_service.buscar_por_id(db, comanda_id)
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.put("/{comanda_id}", response_model=ComandaResponse)
def atualizar(
    comanda_id: int,
    dados: ComandaUpdate,
    db: Session = Depends(get_db),
    user=Depends(get_usuario_autenticado),
):
    try:
        return comanda_service.atualizar(
            db, comanda_id, dados.model_dump(exclude_unset=True)
        )
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.delete("/{comanda_id}")
def deletar(
    comanda_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_usuario_autenticado),
):
    try:
        comanda_service.deletar(db, comanda_id)
        return {"success": {"mensagem": "comanda removida"}}
    except ValueError as e:
        raise HTTPException(404, str(e))
