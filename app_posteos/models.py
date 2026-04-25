from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,func
from app_posteos.database import Base
from sqlalchemy.sql import func


class Posteos(Base):
    __tablename__ = "posteos"
    
    post_id = Column(Integer,primary_key=True,index=True)
    title = Column(String(60),nullable=False)
    contenido = Column(String(500))
    created_at = Column(DateTime,server_default=func.now())
    user_id = Column(Integer,ForeignKey("usuarios.user_id"),nullable=False)
    
    
    
class Usuarios(Base):
    __tablename__ = "usuarios"
    
    user_id = Column(Integer,primary_key=True,index=True)
    nombre = Column(String(40))
    email = Column(String(100))
    contraseña = Column(String(120))