from pydantic import BaseModel
from typing import Optional

class PacienteBase(BaseModel):
    id: Optional[int]
    Nombre: str
    Edad: int
    Genero: str
    Estado_Civil: str
    Ocupacion: str
    Domicilio: str
    Telefono: str
    Correo_Electronico: Optional[str] = None
    Numero_identificacion: str
    class Config:
        orm_mode = True
class Respuesta(BaseModel):
    mensaje:str

