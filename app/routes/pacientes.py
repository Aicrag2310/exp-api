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
    

