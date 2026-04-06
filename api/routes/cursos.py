from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from schemas.curso import CursoCreate, CursoOut
from services.curso_service import (criar_curso, listar_cursos, buscar_curso, alterar_preco_curso)

router = APIRouter(prefix="/cursos", tags=["Cursos"])

class AlterarPrecoInput(BaseModel):
    preco: float

@router.post("", response_model=CursoOut)
def post_curso(data: CursoCreate):
    return criar_curso(data)

@router.get("", response_model=list[CursoOut])
def get_cursos():
    return listar_cursos()

@router.get("/{codigo}", response_model=CursoOut)

def get_curso(codigo: int):
    curso = buscar_curso(codigo)
    if not curso:
        raise HTTPException(status_code=404, detail="Esse curso não está cadastrado!")
    return curso

@router.put("/{codigo}/preco", response_model=CursoOut)
def put_preco_curso(codigo: int, data: AlterarPrecoInput):
    curso = alterar_preco_curso(codigo, data.preco)
    if not curso:
        raise HTTPException(status_code=404, detail="Esse curso não está cadastrado!")
    return curso

@router.get("/{codigo}/preco_final")
def get_preco_final(codigo: int):
    curso = buscar_curso(codigo)
    if not curso:
        raise HTTPException(status_code=404, detail="Esse curso não está cadastrado!")
    return {"codigo": curso.codigo, "titulo": curso.titulo, "preco_final": curso.preco_final()}