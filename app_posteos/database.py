from sqlalchemy.orm import sessionmaker,declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv #Importa la funcion que lee el archivo .env
import os #Importa el modulo para acceder a las variables de entorno
from pathlib import Path #Importa el modulo para manejar rutas de archivos, se usara para construir la ruta al archivo .env de manera mas robusta
load_dotenv(Path(__file__).parent / ".env") #Lee el archivo .env ubicado en el mismo directorio que este archivo y carga las variables de entorno



SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")

Base = declarative_base()

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
