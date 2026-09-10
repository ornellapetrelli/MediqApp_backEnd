from sqlalchemy import Column, Integer, String
from app.database import Base


class Country(Base):
    __tablename__ = "paises"

    id_pais = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    nombre = Column(
        String(100),
        unique=True,
        nullable=False
    )