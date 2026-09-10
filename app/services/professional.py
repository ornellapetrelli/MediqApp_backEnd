from sqlalchemy.orm import Session
# services contiene la logica de negocio, es decir las operaciones que se pueden realizar con los datos.
from app.models import (
    Professional,
    Specialty,
    ProfessionalSpecialty,
    License,
    ProfessionalLicense,
    HealthInsurance,
    ProfessionalHealthInsurance
)

def register_professional(
    db: Session,
    id_usuario: int,
    profesion: str,
    especialidad: str,
    matricula: str,
    tipo_matricula: str,
    provincia_matricula: int,
    universidad_titulo: str,
    anio_graduacion: int
):
    try:
        profesional = Professional(
            id_usuario=id_usuario,
            profesion=profesion,
            universidad_titulo=universidad_titulo,
            anio_graduacion=anio_graduacion
        )

        db.add(profesional)
        # el flush() es para que se ejecute la query y se genere el id_profesional, que es necesario para las relaciones con especialidad y matricula
        db.flush()
        #  aca lo que hago es buscar la especialidad en la base de datos, si no existe la creo y la agrego a la base de datos, evitando duplicados. 
        especialidad_db = db.query(Specialty).filter(
            Specialty.nombre == especialidad
        ).first()

        if especialidad_db is None:
            especialidad_db = Specialty(
                nombre=especialidad
            )
        db.add(especialidad_db)
        db.flush()

        relacion_especialidad = ProfessionalSpecialty(
            id_profesional=profesional.id_profesional,
            id_especialidad=especialidad_db.id_especialidad
        )

        db.add(relacion_especialidad)

        matricula_db = db.query(License).filter(
        License.numero == matricula,
        License.tipo == tipo_matricula,
        License.id_provincia == provincia_matricula
        ).first()   

        if matricula_db is None:
            matricula_db = License(
                numero=matricula,
                tipo=tipo_matricula,
                id_provincia=provincia_matricula
        )

        db.add(matricula_db)
        db.flush()

        relacion_matricula = ProfessionalLicense(
            id_profesional=profesional.id_profesional,
            id_matricula=matricula_db.id_matricula
        )

        db.add(relacion_matricula)
    # commit confirma los cambios y los guarda en la base de datos y refresh actualiza el objeto profesional con los datos de la bd.
        db.commit()
        db.refresh(profesional)

        return profesional
    except Exception:
        print(Exception)
        db.rollback()
        raise


def get_professional(
    db: Session,
    id_profesional: int
):
    profesional = db.query(Professional).filter(
        Professional.id_profesional == id_profesional
    ).first()

    if profesional is None:
        return None

    relacion_especialidad = db.query(ProfessionalSpecialty).filter(
        ProfessionalSpecialty.id_profesional == id_profesional
    ).first()

    especialidad = None

    if relacion_especialidad:
        especialidad = db.query(Specialty).filter(
            Specialty.id_especialidad == relacion_especialidad.id_especialidad
        ).first()

    relacion_matricula = db.query(ProfessionalLicense).filter(
        ProfessionalLicense.id_profesional == id_profesional
    ).first()

    matricula = None

    if relacion_matricula:
        matricula = db.query(License).filter(
            License.id_matricula == relacion_matricula.id_matricula
        ).first()

    return {
        "id_profesional": profesional.id_profesional,
        "id_usuario": profesional.id_usuario,
        "profesion": profesional.profesion,
        "universidad_titulo": profesional.universidad_titulo,
        "anio_graduacion": profesional.anio_graduacion,
        "descripcion": profesional.descripcion,
        "foto_url": profesional.foto_url,
        "modalidad": profesional.modalidad,
        "valor_consulta_particular": profesional.valor_consulta_particular,
        "verificado": profesional.verificado,
        "activo": profesional.activo,
        "especialidad": especialidad.nombre if especialidad else None,
        "matricula": {
            "numero": matricula.numero,
            "tipo": matricula.tipo,
            "id_provincia": matricula.id_provincia
        } if matricula else None
    }

def update_professional(
    db: Session,
    id_profesional: int,
    datos
):
    profesional = db.query(Professional).filter(
        Professional.id_profesional == id_profesional
    ).first()

    if profesional is None:
        return None

    if datos.profesion is not None:
        profesional.profesion = datos.profesion

    if datos.universidad_titulo is not None:
        profesional.universidad_titulo = datos.universidad_titulo

    if datos.anio_graduacion is not None:
        profesional.anio_graduacion = datos.anio_graduacion

    if datos.descripcion is not None:
        profesional.descripcion = datos.descripcion

    if datos.foto_url is not None:
        profesional.foto_url = datos.foto_url

    if datos.modalidad is not None:
        profesional.modalidad = datos.modalidad

    if datos.valor_consulta_particular is not None:
        profesional.valor_consulta_particular = datos.valor_consulta_particular

    db.commit()
    db.refresh(profesional)

    return profesional

def deactivate_professional(
    db: Session,
    id_profesional: int
):
    profesional = db.query(Professional).filter(
        Professional.id_profesional == id_profesional
    ).first()

    if profesional is None:
        return None

    profesional.activo = False

    db.commit()
    db.refresh(profesional)

    return profesional


def add_health_insurance(
    db: Session,
    id_profesional: int,
    id_obra_social: int
):
    profesional = db.query(Professional).filter(
        Professional.id_profesional == id_profesional
    ).first()

    if profesional is None:
        return None

    obra_social = db.query(HealthInsurance).filter(
        HealthInsurance.id_obra_social == id_obra_social
    ).first()

    if obra_social is None:
        return None

    relacion_existente = db.query(
        ProfessionalHealthInsurance
    ).filter(
        ProfessionalHealthInsurance.id_profesional == id_profesional,
        ProfessionalHealthInsurance.id_obra_social == id_obra_social
    ).first()

    if relacion_existente:
        return relacion_existente

    relacion = ProfessionalHealthInsurance(
        id_profesional=id_profesional,
        id_obra_social=id_obra_social
    )

    db.add(relacion)
    db.commit()
    db.refresh(relacion)

    return relacion


def add_health_insurance(
    db: Session,
    id_profesional: int,
    id_obra_social: int
):
    profesional = db.query(Professional).filter(
        Professional.id_profesional == id_profesional
    ).first()

    if profesional is None:
        return None

    obra_social = db.query(HealthInsurance).filter(
        HealthInsurance.id_obra_social == id_obra_social
    ).first()

    if obra_social is None:
        return None

    relacion_existente = db.query(
        ProfessionalHealthInsurance
    ).filter(
        ProfessionalHealthInsurance.id_profesional == id_profesional,
        ProfessionalHealthInsurance.id_obra_social == id_obra_social
    ).first()

    if relacion_existente:
        return relacion_existente

    relacion = ProfessionalHealthInsurance(
        id_profesional=id_profesional,
        id_obra_social=id_obra_social
    )

    db.add(relacion)
    db.commit()
    db.refresh(relacion)

    return relacion

def get_health_insurances(
    db: Session,
    id_profesional: int
):
    profesional = db.query(Professional).filter(
        Professional.id_profesional == id_profesional
    ).first()

    if profesional is None:
        return None

    relaciones = db.query(
        ProfessionalHealthInsurance
    ).filter(
        ProfessionalHealthInsurance.id_profesional == id_profesional,
        ProfessionalHealthInsurance.activo == True
    ).all()

    obras_sociales = []

    for relacion in relaciones:
        obra_social = db.query(HealthInsurance).filter(
            HealthInsurance.id_obra_social == relacion.id_obra_social
        ).first()

        if obra_social:
            obras_sociales.append({
                "id_obra_social": obra_social.id_obra_social,
                "nombre": obra_social.nombre,
                "descripcion": obra_social.descripcion
            })

    return obras_sociales

def deactivate_health_insurance(
    db: Session,
    id_profesional: int,
    id_obra_social: int
):
    relacion = db.query(
        ProfessionalHealthInsurance
    ).filter(
        ProfessionalHealthInsurance.id_profesional == id_profesional,
        ProfessionalHealthInsurance.id_obra_social == id_obra_social
    ).first()

    if relacion is None:
        return None

    relacion.activo = False

    db.commit()
    db.refresh(relacion)

    return relacion

def add_specialty(
    db: Session,
    id_profesional: int,
    id_especialidad: int
):
    profesional = db.query(Professional).filter(
        Professional.id_profesional == id_profesional
    ).first()

    if profesional is None:
        return None

    especialidad = db.query(Specialty).filter(
        Specialty.id_especialidad == id_especialidad,
        Specialty.activo == True
    ).first()

    if especialidad is None:
        return None

    relacion_existente = db.query(
        ProfessionalSpecialty
    ).filter(
        ProfessionalSpecialty.id_profesional == id_profesional,
        ProfessionalSpecialty.id_especialidad == id_especialidad
    ).first()

    if relacion_existente:
        return relacion_existente

    relacion = ProfessionalSpecialty(
        id_profesional=id_profesional,
        id_especialidad=id_especialidad
    )

    db.add(relacion)
    db.commit()
    db.refresh(relacion)

    return relacion

def get_specialties(
    db: Session,
    id_profesional: int
):
    profesional = db.query(Professional).filter(
        Professional.id_profesional == id_profesional
    ).first()

    if profesional is None:
        return None

    relaciones = db.query(
        ProfessionalSpecialty
    ).filter(
        ProfessionalSpecialty.id_profesional == id_profesional
    ).all()

    especialidades = []

    for relacion in relaciones:
        especialidad = db.query(Specialty).filter(
            Specialty.id_especialidad == relacion.id_especialidad,
            Specialty.activo == True
        ).first()

        if especialidad:
            especialidades.append({
                "id_especialidad": especialidad.id_especialidad,
                "nombre": especialidad.nombre,
                "descripcion": especialidad.descripcion
            })

    return especialidades

def remove_specialty(
    db: Session,
    id_profesional: int,
    id_especialidad: int
):
    relacion = db.query(
        ProfessionalSpecialty
    ).filter(
        ProfessionalSpecialty.id_profesional == id_profesional,
        ProfessionalSpecialty.id_especialidad == id_especialidad
    ).first()

    if relacion is None:
        return None

    db.delete(relacion)
    db.commit()

    return relacion

def add_license(
    db: Session,
    id_profesional: int,
    numero: str,
    tipo: str,
    id_provincia: int
):
    profesional = db.query(Professional).filter(
        Professional.id_profesional == id_profesional
    ).first()

    if profesional is None:
        return None

    matricula = db.query(License).filter(
        License.numero == numero,
        License.tipo == tipo,
        License.id_provincia == id_provincia
    ).first()

    if matricula is None:
        matricula = License(
            numero=numero,
            tipo=tipo,
            id_provincia=id_provincia
        )

        db.add(matricula)
        db.flush()

    relacion_existente = db.query(
        ProfessionalLicense
    ).filter(
        ProfessionalLicense.id_profesional == id_profesional,
        ProfessionalLicense.id_matricula == matricula.id_matricula
    ).first()

    if relacion_existente:
        return relacion_existente

    relacion = ProfessionalLicense(
        id_profesional=id_profesional,
        id_matricula=matricula.id_matricula
    )

    db.add(relacion)
    db.commit()
    db.refresh(relacion)

    return relacion

def get_licenses(
    db: Session,
    id_profesional: int
):
    profesional = db.query(Professional).filter(
        Professional.id_profesional == id_profesional
    ).first()

    if profesional is None:
        return None

    relaciones = db.query(
        ProfessionalLicense
    ).filter(
        ProfessionalLicense.id_profesional == id_profesional
    ).all()

    matriculas = []

    for relacion in relaciones:
        matricula = db.query(License).filter(
            License.id_matricula == relacion.id_matricula,
            License.activa == True
        ).first()

        if matricula:
            matriculas.append({
                "id_matricula": matricula.id_matricula,
                "numero": matricula.numero,
                "tipo": matricula.tipo,
                "id_provincia": matricula.id_provincia,
                "fecha_emision": matricula.fecha_emision,
                "fecha_vencimiento": matricula.fecha_vencimiento
            })

    return matriculas

def deactivate_license(
    db: Session,
    id_profesional: int,
    id_matricula: int
):
    relacion = db.query(
        ProfessionalLicense
    ).filter(
        ProfessionalLicense.id_profesional == id_profesional,
        ProfessionalLicense.id_matricula == id_matricula
    ).first()

    if relacion is None:
        return None

    matricula = db.query(License).filter(
        License.id_matricula == id_matricula
    ).first()

    if matricula is None:
        return None

    matricula.activa = False

    db.commit()
    db.refresh(matricula)

    return matricula