from re import S
import db

from sqlalchemy import Column, Integer, String

class User(db.base):
    __tablename__ = 'user' #Nombre de la tabla
    idUser = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    dni = Column(String)
    telefono = Column(String)
    correo = Column(String)
