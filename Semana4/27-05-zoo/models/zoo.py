from sqlalchemy.sql.expression import true
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from ..database import Base
from sqlalchemy import Integer, Column, String, Float

class Zoo(Base):
    __tablename__='zoo'

    idzoo = Column(Integer, primary_key=true)
    nombre = Column(String)
    ciudad = Column(String)
    tamano = Column(Float)
    presupuesto_anual = Column(Float)

    
