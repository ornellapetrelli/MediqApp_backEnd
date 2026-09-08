from app.schemas.auth_schema import Credenciales

def login_paciente_controller(datos : Credenciales):

    return {"message": "Login recibido exitosamente"}

def login_secretaria_controller(datos : Credenciales):
    return {"message" : "Login recibido exitosamente"}