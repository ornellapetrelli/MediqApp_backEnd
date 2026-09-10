from sqlalchemy.orm import Session

from app.schemas.professional import ProfessionalRegister, ProfessionalUpdate, ProfessionalLicenseCreate
from fastapi import HTTPException
from app.services.professional import (
    register_professional,
    get_professional,
    update_professional,
    deactivate_professional,
    add_health_insurance,
    get_health_insurances,
    deactivate_health_insurance,
    add_specialty,
    get_specialties,
    remove_specialty,
    add_license,
    get_licenses,
    deactivate_license
)

def register_professional_controller(
    db: Session,
    datos: ProfessionalRegister,
    id_usuario: int
):
    return register_professional(
        db=db,
        id_usuario=id_usuario,
        profesion=datos.profesion,
        especialidad=datos.especialidad,
        matricula=datos.matricula,
        tipo_matricula=datos.tipo_matricula,
        provincia_matricula=datos.id_provincia,
        universidad_titulo=datos.universidad_titulo,
        anio_graduacion=datos.anio_graduacion
    )


def get_professional_controller(
    db: Session,
    id_profesional: int
):
    profesional = get_professional(
        db=db,
        id_profesional=id_profesional
    )

    if profesional is None:
        raise HTTPException(
            status_code=404,
            detail="Profesional no encontrado"
        )

    return profesional

def update_professional_controller(
    db: Session,
    id_profesional: int,
    datos: ProfessionalUpdate
):
    profesional = update_professional(
        db=db,
        id_profesional=id_profesional,
        datos=datos
    )

    if profesional is None:
        raise HTTPException(
            status_code=404,
            detail="Profesional no encontrado"
        )

    return profesional

def deactivate_professional_controller(
    db: Session,
    id_profesional: int
):
    profesional = deactivate_professional(
        db=db,
        id_profesional=id_profesional
    )

    if profesional is None:
        raise HTTPException(
            status_code=404,
            detail="Profesional no encontrado"
        )

    return profesional

def add_health_insurance_controller(
    db: Session,
    id_profesional: int,
    id_obra_social: int
):
    relacion = add_health_insurance(
        db=db,
        id_profesional=id_profesional,
        id_obra_social=id_obra_social
    )

    if relacion is None:
        raise HTTPException(
            status_code=404,
            detail="Profesional u obra social no encontrada"
        )

    return relacion

def get_health_insurances_controller(
    db: Session,
    id_profesional: int
):
    obras_sociales = get_health_insurances(
        db=db,
        id_profesional=id_profesional
    )

    if obras_sociales is None:
        raise HTTPException(
            status_code=404,
            detail="Profesional no encontrado"
        )

    return obras_sociales

def deactivate_health_insurance_controller(
    db: Session,
    id_profesional: int,
    id_obra_social: int
):
    relacion = deactivate_health_insurance(
        db=db,
        id_profesional=id_profesional,
        id_obra_social=id_obra_social
    )

    if relacion is None:
        raise HTTPException(
            status_code=404,
            detail="Asociación no encontrada"
        )

    return relacion

def add_specialty_controller(
    db: Session,
    id_profesional: int,
    id_especialidad: int
):
    relacion = add_specialty(
        db=db,
        id_profesional=id_profesional,
        id_especialidad=id_especialidad
    )

    if relacion is None:
        raise HTTPException(
            status_code=404,
            detail="Profesional o especialidad no encontrada"
        )

    return relacion

def get_specialties_controller(
    db: Session,
    id_profesional: int
):
    especialidades = get_specialties(
        db=db,
        id_profesional=id_profesional
    )

    if especialidades is None:
        raise HTTPException(
            status_code=404,
            detail="Profesional no encontrado"
        )

    return especialidades

def remove_specialty_controller(
    db: Session,
    id_profesional: int,
    id_especialidad: int
):
    relacion = remove_specialty(
        db=db,
        id_profesional=id_profesional,
        id_especialidad=id_especialidad
    )

    if relacion is None:
        raise HTTPException(
            status_code=404,
            detail="Especialidad no asociada al profesional"
        )

    return {
        "message": "Especialidad desasociada correctamente"
    }

def add_license_controller(
    db: Session,
    id_profesional: int,
    datos: ProfessionalLicenseCreate
):
    relacion = add_license(
        db=db,
        id_profesional=id_profesional,
        numero=datos.numero,
        tipo=datos.tipo,
        id_provincia=datos.id_provincia
    )

    if relacion is None:
        raise HTTPException(
            status_code=404,
            detail="Profesional no encontrado"
        )

    return relacion

def get_licenses_controller(
    db: Session,
    id_profesional: int
):
    matriculas = get_licenses(
        db=db,
        id_profesional=id_profesional
    )

    if matriculas is None:
        raise HTTPException(
            status_code=404,
            detail="Profesional no encontrado"
        )

    return matriculas

def deactivate_license_controller(
    db: Session,
    id_profesional: int,
    id_matricula: int
):
    matricula = deactivate_license(
        db=db,
        id_profesional=id_profesional,
        id_matricula=id_matricula
    )

    if matricula is None:
        raise HTTPException(
            status_code=404,
            detail="Matrícula no encontrada"
        )

    return matricula