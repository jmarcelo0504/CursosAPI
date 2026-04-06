from fastapi import FastAPI
from api.routes.alunos import router as alunos_router
from api.routes.cursos import router as cursos_router

app = FastAPI(title="Cursos do Gordinho")

@app.get("/")
def home():
    return {"msg": "Cursos do gordinho aplicáveis."}

app.include_router(alunos_router)
app.include_router(cursos_router)