from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.schemas.professional import ProfessionalRegister, ProfessionalUpdate,ProfessionalLicenseCreate
from app.controllers.professional import register_professional_controller
from app.controllers.professional import get_professional_controller
from app.controllers.professional import update_professional_controller
from app.controllers.professional import deactivate_professional_controller
from app.controllers.professional import add_health_insurance_controller
from app.controllers.professional import get_health_insurances_controller
from app.controllers.professional import deactivate_health_insurance_controller
from app.controllers.professional import add_specialty_controller
from app.controllers.professional import get_specialties_controller
from app.controllers.professional import remove_specialty_controller
from app.controllers.professional import add_license_controller
from app.controllers.professional import get_licenses_controller
from app.controllers.professional import deactivate_license_controller

router = APIRouter(
    prefix="/profesional",
    tags=["Profesionales"]
)


def get_db():
    db = SessionLocal()

    try:
        # yield se la entrega al endpoint, la funcion que llama a este get_db() va a recibir el dbb como parametro, se termina de ejecutar y se ejecuta el finally(cieerra la conexion)
        yield db
    finally:
        db.close()


@router.post("/registro")
def register_professional(
    datos: ProfessionalRegister,
    db: Session = Depends(get_db)
):
    return register_professional_controller(
        db=db,
        datos=datos,
        id_usuario=1
    )

@router.get("/{id_profesional}")
def get_professional(
    id_profesional: int,
    db: Session = Depends(get_db)
):
    return get_professional_controller(
        db=db,
        id_profesional=id_profesional
    )

@router.put("/{id_profesional}")
def update_professional(
    id_profesional: int,
    datos: ProfessionalUpdate,
    db: Session = Depends(get_db)
):
    return update_professional_controller(
        db=db,
        id_profesional=id_profesional,
        datos=datos
    )

@router.delete("/{id_profesional}")
def deactivate_professional(
    id_profesional: int,
    db: Session = Depends(get_db)
):
    return deactivate_professional_controller(
        db=db,
        id_profesional=id_profesional
    )

@router.post("/{id_profesional}/obras-sociales/{id_obra_social}")
def add_health_insurance(
    id_profesional: int,
    id_obra_social: int,
    db: Session = Depends(get_db)
):
    return add_health_insurance_controller(
        db=db,
        id_profesional=id_profesional,
        id_obra_social=id_obra_social
    )

@router.get("/{id_profesional}/obras-sociales")
def get_health_insurances(
    id_profesional: int,
    db: Session = Depends(get_db)
):
    return get_health_insurances_controller(
        db=db,
        id_profesional=id_profesional
    )

@router.delete("/{id_profesional}/obras-sociales/{id_obra_social}")
def deactivate_health_insurance(
    id_profesional: int,
    id_obra_social: int,
    db: Session = Depends(get_db)
):
    return deactivate_health_insurance_controller(
        db=db,
        id_profesional=id_profesional,
        id_obra_social=id_obra_social
    )
@router.post("/{id_profesional}/especialidades/{id_especialidad}")
def add_specialty(
    id_profesional: int,
    id_especialidad: int,
    db: Session = Depends(get_db)
):
    return add_specialty_controller(
        db=db,
        id_profesional=id_profesional,
        id_especialidad=id_especialidad
    )

@router.get("/{id_profesional}/especialidades")
def get_specialties(
    id_profesional: int,
    db: Session = Depends(get_db)
):
    return get_specialties_controller(
        db=db,
        id_profesional=id_profesional
    )

@router.delete("/{id_profesional}/especialidades/{id_especialidad}")
def remove_specialty(
    id_profesional: int,
    id_especialidad: int,
    db: Session = Depends(get_db)
):
    return remove_specialty_controller(
        db=db,
        id_profesional=id_profesional,
        id_especialidad=id_especialidad
    )

@router.post("/{id_profesional}/matriculas")
def add_license(
    id_profesional: int,
    datos: ProfessionalLicenseCreate,
    db: Session = Depends(get_db)
):
    return add_license_controller(
        db=db,
        id_profesional=id_profesional,
        datos=datos
    )

@router.get("/{id_profesional}/matriculas")
def get_licenses(
    id_profesional: int,
    db: Session = Depends(get_db)
):
    return get_licenses_controller(
        db=db,
        id_profesional=id_profesional
    )

@router.delete("/{id_profesional}/matriculas/{id_matricula}")
def deactivate_license(
    id_profesional: int,
    id_matricula: int,
    db: Session = Depends(get_db)
):
    return deactivate_license_controller(
        db=db,
        id_profesional=id_profesional,
        id_matricula=id_matricula
    )