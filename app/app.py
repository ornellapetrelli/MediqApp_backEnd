from app.database import Base, engine
from fastapi import FastAPI
from app.routers.auth_router import router as auth_router
from app.routers.professional import router as professional_router
app = FastAPI()

Base.metadata.create_all(bind=engine)


app.include_router(auth_router)
app.include_router(professional_router)

@app.get("/")
def root():
    return {"message": "mediqApp  Backend Funcionando"}
