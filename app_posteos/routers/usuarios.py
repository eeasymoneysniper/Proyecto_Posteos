from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app_posteos.database import get_db
from app_posteos.models import Usuarios
from app_posteos.schemas import UsuarioCreate,UsuarioResponse,UsuarioLogin
from typing import Annotated


router = APIRouter()

@router.post("/usuarios/",response_model=UsuarioResponse)
async def create_usuario(usuario: UsuarioCreate,db: Annotated[Session,Depends(get_db)]):
    db_usuario = db.query(Usuarios).filter(Usuarios.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="El correo ya está registrado")
    
    nuevo_usuario = Usuarios(nombre=usuario.nombre,email=usuario.email,contraseña=usuario.contraseña)
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return nuevo_usuario

@router.post("/usuarios/login",response_model=UsuarioLogin)
async def login_usuario(usuario:UsuarioLogin,db : Annotated[Session,Depends(get_db)]):
    db_user = db.query(Usuarios).filter(Usuarios.email == usuario.email).first()
    if not db_user or db_user.contraseña != usuario.contraseña:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Credenciales inválidas")
    return usuario


@router.get("/usuarios/get/{user_id}",response_model=UsuarioResponse)
async def get_user(user_id : int,db : Annotated[Session,Depends(get_db)]):
    db_user = db.query(Usuarios).filter(Usuarios.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")
    return db_user

