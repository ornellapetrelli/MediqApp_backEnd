from sqlalchemy import Column, BigInteger, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base


class ProfessionalHealthInsurance(Base):
    __tablename__ = "profesional_obra_social"

    id_profesional = Column(
        BigInteger,
        ForeignKey("profesionales.id_profesional"),
        primary_key=True
    )

    id_obra_social = Column(
        Integer,
        ForeignKey("obras_sociales.id_obra_social"),
        primary_key=True
    )

    activo = Column(
        Boolean,
        default=True,
        nullable=False
    )

    profesional = relationship(
        "Professional",
        back_populates="obras_sociales"
    )

    obra_social = relationship(
        "HealthInsurance"
    )