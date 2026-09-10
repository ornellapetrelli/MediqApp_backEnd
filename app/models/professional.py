from sqlalchemy import Column, BigInteger, String, Text, Boolean, Integer, Numeric
from sqlalchemy.orm import relationship
from app.database import Base

# EL MODELS ES EL QUE DEFINE LA ESTRCUTURA DE LA TABLA EN LA BASE DE DATOS, ES DECIR, LOS CAMPOS Y SUS DATOS.

class Professional(Base):
    __tablename__ = "profesionales"

    id_profesional = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    id_usuario = Column(
        BigInteger,
        nullable=False,
        unique=True
    )

    profesion = Column(
        String(150),
        nullable=False
    )

    universidad_titulo = Column(
        String(200),
        nullable=False
    )

    anio_graduacion = Column(
        Integer,
        nullable=False
    )

    descripcion = Column(
        Text,
        nullable=True
    )

    foto_url = Column(
        String(500),
        nullable=True
    )

    modalidad = Column(
        String(20),
        nullable=True
    )

    valor_consulta_particular = Column(
        Numeric(10, 2),
        nullable=True
    )

    verificado = Column(
        Boolean,
        default=False,
        nullable=False
    )

    activo = Column(
        Boolean,
        default=True,
        nullable=False
    )

    especialidades = relationship(
        "ProfessionalSpecialty",
        back_populates="profesional"
    )

    matriculas = relationship(
        "ProfessionalLicense",
        back_populates="profesional"
    )

    obras_sociales = relationship(
        "ProfessionalHealthInsurance",
        back_populates="profesional"
    )