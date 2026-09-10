from sqlalchemy import Column, Integer, String, Date

from app.database import Base

class Usuario(Base):

    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    usuario = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    dni = Column(String, unique=True, nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    telefono = Column(String, nullable=False)
    password_hash = Column(String, nullable=False)