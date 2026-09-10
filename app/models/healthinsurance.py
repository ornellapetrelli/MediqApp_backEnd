from sqlalchemy import Column, Integer, String, Text, Boolean
from app.database import Base


class HealthInsurance(Base):
    __tablename__ = "obras_sociales"

    id_obra_social = Column(
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