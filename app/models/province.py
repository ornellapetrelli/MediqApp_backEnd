from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Province(Base):
    __tablename__ = "provincias"

    id_provincia = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    id_pais = Column(
        Integer,
        ForeignKey("paises.id_pais"),
        nullable=False
    )

    nombre = Column(
        String(100),
        nullable=False
    )