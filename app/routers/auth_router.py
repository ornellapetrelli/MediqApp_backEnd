from fastapi import APIRouter
from app.schemas.auth_schema import Credenciales, Registro 
from app.controllers.auth_controller import (
    login_paciente_controller,
    login_secretaria_controller,
    registro_paciente_controller,
    registro_secretaria_controller
)

router = APIRouter()

@router.post("/paciente/login")
def login_paciente(datos : Credenciales):
  return login_paciente_controller(datos)

@router.post("/secretaria/login")
def login_secretaria(datos: Credenciales):
  return login_secretaria_controller(datos)

@router.post("/paciente/registro")
def registro_paciente(datos: Registro):
  return registro_paciente_controller(datos)

@router.post("/secretaria/registro")
def registro_secretaria(datos: Registro):
  return registro_secretaria_controller(datos)