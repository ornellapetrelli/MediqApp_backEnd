from pydantic import BaseModel
from pydantic import BaseModel, EmailStr
from datetime import date

# datos que le digo a la api que retorne cuando le pido un profesional

class ProfessionalRegister(BaseModel):
    usuario: str
    password: str
    nombre: str
    apellido: str
    dni: str
    fecha_nacimiento: date
    email: EmailStr
    telefono: str
    profesion: str
    especialidad: str
    matricula: str
    tipo_matricula: str
    id_provincia: int
    universidad_titulo: str
    anio_graduacion: int

class ProfessionalUpdate(BaseModel):
    profesion: str | None = None
    universidad_titulo: str | None = None
    anio_graduacion: int | None = None
    descripcion: str | None = None
    foto_url: str | None = None
    modalidad: str | None = None
    valor_consulta_particular: float | None = None

class ProfessionalLicenseCreate(BaseModel):
    numero: str
    tipo: str
    id_provincia: int