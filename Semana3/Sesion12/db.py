from sqlalchemy import create_engine, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

# cadena de conexion    mysql+pymysql:////usuario:contralocalhost/nombreDeLaBd
engine = create_engine("mysql+pymysql://root:root@localhost/usersdb")

base = declarative_base()

Session = sessionmaker(bind=engine)