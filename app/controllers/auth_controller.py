from fastapi import HTTPException

from app.schemas.auth_schema import Credenciales, Registro
from app.models.usuario_model import Usuario
from app.database import SessionLocal
from app.utils.security import hashear_password, verificar_password


def registro_controller(datos: Registro):

    db = SessionLocal()

    try:
        usuario_existente = (
            db.query(Usuario)
            .filter(Usuario.usuario == datos.usuario)
            .first()
        )

        if usuario_existente:
            raise HTTPException(
                status_code=400,
                detail="El nombre de usuario ya está registrado"
            )

        email_existente = (
            db.query(Usuario)
            .filter(Usuario.email == datos.email)
            .first()
        )

        if email_existente:
            raise HTTPException(
                status_code=400,
                detail="El email ya está registrado"
            )

        dni_existente = (
            db.query(Usuario)
            .filter(Usuario.dni == datos.dni)
            .first()
        )

        if dni_existente:
            raise HTTPException(
                status_code=400,
                detail="El DNI ya está registrado"
            )

        password_hasheada = hashear_password(datos.password)

        nuevo_usuario = Usuario(
            nombre=datos.nombre,
            apellido=datos.apellido,
            usuario=datos.usuario,
            email=datos.email,
            dni=datos.dni,
            fecha_nacimiento=datos.fecha_nacimiento,
            telefono=datos.telefono,
            password_hash=password_hasheada
        )

        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)

        return {
            "message": "Usuario registrado exitosamente",
            "id": nuevo_usuario.id
        }
    finally:
        db.close()


def login_controller(datos: Credenciales):

    db = SessionLocal()

    try:
        usuario = (
            db.query(Usuario)
            .filter(Usuario.usuario == datos.usuario)
            .first()
        )

        if not usuario:
            raise HTTPException(
                status_code=401,
                detail="Usuario o contraseña incorrectos"
            )

        password_correcta = verificar_password(
            datos.password,
            usuario.password_hash
        )

        if not password_correcta:
            raise HTTPException(
                status_code=401,
                detail="Usuario o contraseña incorrectos"
            )

        return {
            "message": "Login exitoso",
            "id": usuario.id,
            "usuario": usuario.usuario
        }

    finally:
        db.close()