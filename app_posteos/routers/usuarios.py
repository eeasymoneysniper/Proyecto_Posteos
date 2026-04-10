from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from app_posteos.database import get_db
from app_posteos.models import Usuarios
