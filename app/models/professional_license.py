from sqlalchemy import Column, BigInteger, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class ProfessionalLicense(Base):
    __tablename__ = "profesional_matricula"

    id_profesional = Column(
        BigInteger,
        ForeignKey("profesionales.id_profesional"),
        primary_key=True
    )

    id_matricula = Column(
        BigInteger,
        ForeignKey("matriculas.id_matricula"),
        primary_key=True
    )

    profesional = relationship(
        "Professional",
        back_populates="matriculas"
    )

    matricula = relationship(
        "License"
    )