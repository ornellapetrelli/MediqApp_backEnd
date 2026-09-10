from fastapi import APIRouter

from app.schemas.auth_schema import Credenciales, Registro

from app.controllers.auth_controller import (
    login_controller,
    registro_controller
)

router = APIRouter()

@router.post("/login")
def login(datos: Credenciales):
    return login_controller(datos)


@router.post("/registro")
def registro(datos: Registro):
    return registro_controller(datos)