from domain.aluno import Aluno
from domain.curso import Curso
from repositories.memory import db

def criar_aluno(data):
    aluno = Aluno(id=data.id, nome=data.nome, email=data.email)
    db.alunos[aluno.id] = aluno
    return aluno

def listar_alunos():
    return list(db.alunos.values())

def criar_curso(data):
    curso = Curso(codigo=data.codigo, titulo=data.titulo, preco=data.preco, tipo=data.tipo, desconto_percentual=data.desconto_percentual)
    db.cursos[curso.codigo] = curso
    return curso

def listar_cursos():
    return list(db.cursos.values())

def buscar_curso(codigo: int):
    return db.cursos.get(codigo)

def alterar_preco_curso(codigo: int, novo_preco: float):
    livro = db.cursos.get(codigo)
    if not curso:
        return None
    if novo_preco < 0:
        raise ValueError("O preço não pode ser negativo!")
    curso.preco = novo_preco
    return curso