from sqlalchemy import Column, Integer, String
from ...db.Conexion import Base

class User(Base):
    __tablename__ = 'usuarios'
    id  = Column(Integer, primary_key=True, index=True)
    username = Column(String(50))
    password = Column(String(50))
    email = Column(String(100))