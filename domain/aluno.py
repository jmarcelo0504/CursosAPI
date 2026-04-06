from dataclasses import dataclass

@dataclass (frozen=True)
class Aluno:
    id: int
    nome: str
    email: str