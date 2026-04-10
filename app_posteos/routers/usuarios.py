from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app_posteos.database import get_db
from app_posteos.models import Usuarios
from app_posteos.schemas import UsuarioCreate,UsuarioResponse,UsuarioLogin
from typing import Annotated


router = APIRouter()