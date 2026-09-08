from fastapi import APIRouter
from app.schemas.auth_schema import Credenciales

router = APIRouter()


@router.post("/pacientes/login")

def login_paciente(datos : Credenciales):

    return {"message": "Login recibido exitosamente"}


