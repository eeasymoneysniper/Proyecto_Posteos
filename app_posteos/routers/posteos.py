from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app_posteos.database import get_db
from app_posteos.models import Posteos,Usuarios
from app_posteos.schemas import posteoCreate,posteoResponse
from typing import Annotated

router = APIRouter()    

@router.post("/posteos/",response_model=posteoResponse)
async def create_posteo(posteo : posteoCreate,user_id : int ,db : Annotated[Session,Depends(get_db)]):
    
    user = db.query(Usuarios).filter(Usuarios.user_id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no existe")
    nuevo_posteo = Posteos(title=posteo.title,contenido=posteo.contenido,user_id=user_id)
    db.add(nuevo_posteo)
    db.commit()
    db.refresh(nuevo_posteo)
    return nuevo_posteo

@router.get("/posteos/all",response_model=list[posteoResponse])
async def get_posteos(db : Annotated[Session,Depends(get_db)]):
    return db.query(Posteos).all()

@router.get("/posteos/{user_id}",response_model=posteoResponse)
async def get_posteo(user_id : int,db : Annotated[Session,Depends(get_db)]):
    usuario = db.query(Usuarios).filter(Usuarios.user_id == user_id).first()
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="usuario no Encontrado")
    posteo = db.query(Posteos).filter(Posteos.user_id == user_id).first()
    if not posteo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Posteo no Encontrado")
    return posteo
   