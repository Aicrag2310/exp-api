from fastapi import APIRouter, HTTPException
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from settings import get_settings
from app.models.usuarios import models
from app.schemas.usuarios_s import schemas
from app.db.Conexion import SessionLocal,engine
from sqlalchemy.orm import Session
from typing import List
from ..db.Conexion import get_db
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()



#Validar
@router.post('/login/', response_model=schemas.User)
def login(user: schemas.User_Validate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    # verificar si el usuario existe
    if not db_user:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')

    # verificar si la contraseña es correcta
    if db_user.password != user.password:
        raise HTTPException(status_code=401, detail='Contraseña incorrecta')

    # si todo está bien, devolver el usuario
    return db_user
@router.get('/usuarios/',response_model=List[schemas.User])
def show_users(db:Session=Depends(get_db)):
    usuarios = db.query(models.User).all()
    return usuarios

@router.post('/usuarios/',response_model=schemas.User)
def create_users(entrada:schemas.User, db:Session=Depends(get_db)):
    usuario = models.User(
        username = entrada.username,
        password = entrada.password,
        email = entrada.email
        )
    db.add(usuario)
    db.commit()
    return usuario

@router.put('/usuarios/{usuario_id}',response_model=schemas.User)
def update_users(usuario_id:int, entrada:schemas.User, db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter_by(id=usuario_id).first()
    usuario.username = entrada.username
    usuario.password = entrada.password
    usuario.email = entrada.email
    db.commit()
    db.refresh()
    return usuario

@router.delete('/usuarios/{usuario_id}',response_model=schemas.Respuesta)
def delete_users(usuario_id:int, db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter_by(id=usuario_id).first()
    db.delete(usuario)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado Correctamente")
    return respuesta