from pydantic import BaseModel, EmailStr
from datetime import date 

class Credenciales(BaseModel):
    usuario : str
    password : str

class Registro (BaseModel):
    nombre : str
    apellido : str
    usuario : str
    email : EmailStr
    dni : str 
    fecha_nacimiento : date 
    telefono :str
    password : str



