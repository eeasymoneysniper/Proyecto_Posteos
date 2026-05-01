from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app_posteos.database import get_db
from app_posteos.models import Usuarios
from app_posteos.schemas import UsuarioCreate,UsuarioResponse,UsuarioLogin
from typing import Annotated
import jwt
from datetime import datetime,timezone,timedelta
from pwdlib import PasswordHash
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from dotenv import load_dotenv
import os

oauth2=OAuth2PasswordBearer(tokenUrl="/usuarios/login")

router = APIRouter()

load_dotenv()

CLAVE = os.getenv("CLAVE")
ALGORITMO = os.getenv("ALGORITMO")
EXPIRACION = 1

password_hash = PasswordHash.recommended()


@router.post("/usuarios/",response_model=UsuarioResponse)
async def create_usuario(usuario: UsuarioCreate,db: Annotated[Session,Depends(get_db)]):
    db_usuario = db.query(Usuarios).filter(Usuarios.email == usuario.email).first()
    if db_usuario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="El correo ya está registrado")
    
    nuevo_usuario = Usuarios(nombre=usuario.nombre,email=usuario.email,contraseña=get_password_hashed(usuario.contraseña))
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    
    return nuevo_usuario

@router.post("/usuarios/login")
async def login_usuario(form :Annotated[OAuth2PasswordRequestForm,Depends()],db : Annotated[Session,Depends(get_db)]):
    db_user = db.query(Usuarios).filter(Usuarios.email == form.username).first()
    if not db_user or not verify(form.password,db_user.contraseña):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Credenciales inválidas")
    return {"access_token": create_access_token(data={"sub": db_user.email}), "token_type": "bearer"}


@router.get("/usuarios/get/{user_id}",response_model=UsuarioResponse)
async def get_user(user_id : int,db : Annotated[Session,Depends(get_db)]):
    db_user = db.query(Usuarios).filter(Usuarios.user_id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Usuario no encontrado")
    return db_user

def create_access_token(data: dict):
    expire = datetime.now(timezone.utc) + timedelta(hours=EXPIRACION)
    data["exp"] = expire
    encoded_jwt = jwt.encode(data, CLAVE, algorithm=ALGORITMO)
    
    return encoded_jwt


def verify(plain_password,hashed_password):
    return password_hash.verify(plain_password,hashed_password)

def get_password_hashed(password):
    return password_hash.hash(password)

def get_current_user(token: Annotated[str,Depends(oauth2)],db: Annotated[Session,Depends(get_db)]):
    exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="No se pudo validar las credenciales",headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, CLAVE, algorithms=[ALGORITMO])
        email = payload.get("sub")
        if email is None:
            raise exception
    except jwt.PyJWTError:
        raise exception
    user = db.query(Usuarios).filter(Usuarios.email == email).first()
    if user is None:
        raise exception
    return user