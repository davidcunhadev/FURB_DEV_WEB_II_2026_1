from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_usuario_autenticado
from app.schemas.produto_schema import ProdutoCreate, ProdutoResponse
from app.services import produto_service

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.post("/", response_model=ProdutoResponse, status_code=201)
def criar(
    produto: ProdutoCreate,
    db: Session = Depends(get_db),
    user=Depends(get_usuario_autenticado),
):
    return produto_service.criar(db, produto.model_dump())


@router.get("/", response_model=list[ProdutoResponse])
def listar(
    db: Session = Depends(get_db),
    user=Depends(get_usuario_autenticado),
):
    return produto_service.listar(db)


@router.get("/{produto_id}", response_model=ProdutoResponse)
def buscar_por_id(
    produto_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_usuario_autenticado),
):
    try:
        return produto_service.buscar_por_id(db, produto_id)
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.put("/{produto_id}", response_model=ProdutoResponse)
def atualizar(
    produto_id: int,
    dados: ProdutoCreate,
    db: Session = Depends(get_db),
    user=Depends(get_usuario_autenticado),
):
    try:
        return produto_service.atualizar(db, produto_id, dados.model_dump())
    except ValueError as e:
        raise HTTPException(404, str(e))


@router.delete("/{produto_id}")
def deletar(
    produto_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_usuario_autenticado),
):
    try:
        produto_service.deletar(db, produto_id)
        return {"message": "Produto deletado"}
    except ValueError as e:
        raise HTTPException(404, str(e))
