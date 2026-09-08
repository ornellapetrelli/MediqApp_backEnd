from fastapi import APIRouter
from app.schemas.auth_schema import Credenciales
from app.controllers.auth_controller import (
    login_paciente_controller,
    login_secretaria_controller
)

router = APIRouter()

@router.post("/paciente/login")

@router.post("/secretaria/login")

def login_paciente(datos : Credenciales):
  return login_paciente_controller(datos)

def login_secretaria(datos: Credenciales):
  return login_secretaria_controller(datos)