from pydantic import BaseModel

class UsuarioLogin(BaseModel):
    email : str
    contraseña : str
    
    
class UsuarioCreate(BaseModel):
    nombre : str
    email : str
    contraseña : str
    
    
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
    created_at : str
    user_id : int
    
    class Config:
        from_attributes = True

