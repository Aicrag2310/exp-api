from sqlalchemy import Column, Integer, String
from ...db.Conexion import Base
class Paciente(Base):
    __tablename__  = 'pacientes'
    id = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(200))
    Edad = Column(Integer)
    Genero = Column(String(50))
    Estado_Civil = Column(String(50))
    Ocupacion = Column(String(100))
    Domicilio = Column(String(100))
    Telefono = Column(String(200))
    Correo_Electronico = Column(String(100))
    Numero_identificacion = Column(Integer)