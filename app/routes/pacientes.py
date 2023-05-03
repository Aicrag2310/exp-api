from fastapi import APIRouter, HTTPException
from app.schemas.pacientes_schemas import pacientes_schemas
from ..db.Conexion import get_db
from app.models.pacientes import model_paciente
from sqlalchemy.orm import Session
from fastapi.params import Depends
from typing import List
from fastapi.encoders import jsonable_encoder

router = APIRouter()


# Ruta para obtener todos los pacientes
@router.get('/pacientes/',response_model=List[pacientes_schemas.PacienteBase])
def show_users(db:Session=Depends(get_db)):
   pacientes = db.query(model_paciente.Paciente).all()
   return pacientes


@router.post('/pacientes/',response_model=pacientes_schemas.PacienteBase)
def create_pacientes(entrada:pacientes_schemas.PacienteBase, db:Session=Depends(get_db)):
   print("Datos recibidos:",entrada)
   pacientes = model_paciente.Paciente(
      Nombre = entrada.Nombre,
      Edad = entrada.Edad,
      Genero = entrada.Genero,
      Estado_Civil = entrada.Estado_Civil,
      Ocupacion = entrada.Ocupacion,
      Domicilio = entrada.Domicilio,
      Telefono = entrada.Telefono,
      Correo_Electronico = entrada.Correo_Electronico,
      Numero_identificacion = entrada.Numero_identificacion,
   )
   db.add(pacientes)
   db.commit()
   return pacientes


@router.delete('/pacientes/{paciente_id}',response_model=pacientes_schemas.Respuesta)
def delete_users(paciente_id:int, db:Session=Depends(get_db)):
   paciente = db.query(model_paciente.Paciente).filter_by(id=paciente_id).first()
   db.delete(paciente)
   db.commit()
   respuesta = pacientes_schemas.Respuesta(mensaje="Eliminado Correctamente")
   return respuesta