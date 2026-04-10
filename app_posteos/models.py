from sqlalchemy import Column,Integer,String,ForeignKey,DateTime
from database import Base
from datetime import datetime,timezone


class Posteos(Base):
    __tablename__ = "posteos"
    
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(60))
    contenido = Column(String(500))
    created_at = Column(DateTime,default=datetime.now(timezone.utc))
    user_id = Column(Integer,ForeignKey("usuarios.user_id"))
    
    
    
class Usuarios(Base):
    __tablename__ = "usuarios"
    
    user_id = Column(Integer,primary_key=True,index=True)
    nombre = Column(String(40))
    email = Column(String(100))
    contraseña = Column(String(120))