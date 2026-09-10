from sqlalchemy import Column, BigInteger, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class ProfessionalSpecialty(Base):
    __tablename__ = "profesional_especialidad"

    id_profesional = Column(
        BigInteger,
        ForeignKey("profesionales.id_profesional"),
        primary_key=True
    )

    id_especialidad = Column(
        Integer,
        ForeignKey("especialidades.id_especialidad"),
        primary_key=True
    )

    profesional = relationship(
        "Professional",
        back_populates="especialidades"
    )

    especialidad = relationship(
        "Specialty"
    )