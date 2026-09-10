from sqlalchemy import Column, Integer, String, Text, Boolean
from app.database import Base

class Specialty(Base):
    __tablename__ = "especialidades"

    id_especialidad = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    nombre = Column(
        String(150),
        unique=True,
        nullable=False
    )

    descripcion = Column(
        Text,
        nullable=True
    )

    activo = Column(
        Boolean,
        default=True,
        nullable=False
    )