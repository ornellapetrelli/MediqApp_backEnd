from sqlalchemy import Column, BigInteger, Integer, String, Date, Boolean, ForeignKey
from app.database import Base


class License(Base):
    __tablename__ = "matriculas"

    id_matricula = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    numero = Column(
        String(100),
        nullable=False
    )

    tipo = Column(
        String(50),
        nullable=False
    )

    id_provincia = Column(
        Integer,
        ForeignKey("provincias.id_provincia"),
        nullable=True
    )

    fecha_emision = Column(
        Date,
        nullable=True
    )

    fecha_vencimiento = Column(
        Date,
        nullable=True
    )

    activa = Column(
        Boolean,
        default=True,
        nullable=False
    )