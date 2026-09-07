from pydantic import BaseModel, EmailStr

class Credenciales(BaseModel):
    usuario : str
    password : str

    