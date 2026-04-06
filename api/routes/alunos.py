from fastapi import APIRouter
from schemas.aluno import AlunoCreate, AlunoOut
from services.curso_service import criar_aluno, listar_alunos

router = APIRouter(prefix="/alunos", tags=["Alunos"])

@router.post("", response_model=AlunoOut)
def post_aluno(data: AlunoCreate):
    return criar_aluno(data)

@router.get("", response_model=list[AlunoOut])
def get_alunos():
    return listar_alunos()