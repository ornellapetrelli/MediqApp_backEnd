from app.schemas.auth_schema import Credenciales, Registro

def login_paciente_controller(datos : Credenciales):

    return {"message": "Login recibido exitosamente"}

def login_secretaria_controller(datos : Credenciales):
    return {"message" : "Login recibido exitosamente"}

def registro_paciente_controller(datos : Registro):
    return {"message" : "Registro realizado exitosamente"}

def registro_secretaria_controller(datos : Registro):
    return {"message" : "Registro realizado exitosamente"}