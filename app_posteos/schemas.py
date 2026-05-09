from pydantic import BaseModel
from datetime import datetime,timezone

class UsuarioLogin(BaseModel):
    email : str
    contraseña : str
    
    
class UsuarioCreate(BaseModel):
    nombre : str
    email : str
    contraseña : str

class UsuarioUpdate(BaseModel):
    nombre: str | None = None
    email: str | None = None
    contraseña: str | None = None
    
class UsuarioResponse(BaseModel):
    user_id : int
    nombre : str
    email : str
    
    class Config:
        from_attributes = True
        
        
class posteoCreate(BaseModel):
    title : str
    contenido : str
    

    
class posteoResponse(BaseModel):
    post_id : int
    title : str
    contenido : str
    created_at : datetime=datetime.now(timezone.utc)
    user_id : int 
    
    class Config:
        from_attributes = True


class posteoPut(BaseModel):
    title : str
    contenido : str
    
class posteoDelete(BaseModel):
    post_id : int
