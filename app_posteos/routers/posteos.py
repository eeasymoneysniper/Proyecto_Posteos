from fastapi import APIRouter,Depends,HTTPException,status
from sqlalchemy.orm import Session
from app_posteos.database import get_db
from app_posteos.models import Posteos,Usuarios
from app_posteos.schemas import posteoCreate,posteoResponse,posteoPut,posteoDelete
from typing import Annotated
from app_posteos.routers.usuarios import get_current_user

router = APIRouter()    

@router.post("/posteos/",response_model=posteoResponse)
async def create_posteo(posteo : posteoCreate,db : Annotated[Session,Depends(get_db)],current_user : Annotated[Usuarios,Depends(get_current_user)]):
    
    nuevo_posteo = Posteos(title=posteo.title,contenido=posteo.contenido,user_id=current_user.user_id)
    db.add(nuevo_posteo)
    db.commit()
    db.refresh(nuevo_posteo)
    return nuevo_posteo

@router.get("/posteos/",response_model=list[posteoResponse])
async def get_posteos(db : Annotated[Session,Depends(get_db)],skip=1,limit=1):
    return db.query(Posteos).offset(skip).limit(limit).all()

@router.get("/usuarios/{user_id}/posteos",response_model=list[posteoResponse])
async def get_posteo(user_id : int,db : Annotated[Session,Depends(get_db)]):
    posteo = db.query(Posteos).filter(Posteos.user_id == user_id).all()
    if not posteo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No tiene Posteos registrados")
    return posteo

@router.put("/posteos/{post_id}",response_model=posteoResponse)
async def update_posteo(post_id : int,posteo : posteoPut,db : Annotated[Session,Depends(get_db)],current_user : Annotated[Usuarios,Depends(get_current_user)]):
    db_posteo = db.query(Posteos).filter(Posteos.post_id == post_id).first()
    if not db_posteo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Posteo no encontrado")
    
    if db_posteo.user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="No tienes permiso para modificar este posteo")
    
    db_posteo.title = posteo.title
    db_posteo.contenido = posteo.contenido
    db.commit()
    db.refresh(db_posteo)
    return db_posteo

@router.delete("/posteos/{post_id}")
async def delete_posteo(post_id : int,db : Annotated[Session,Depends(get_db)],current_user : Annotated[Usuarios,Depends(get_current_user)]):
    db_posteo=db.query(Posteos).filter(Posteos.post_id == post_id).first()
    if not db_posteo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Posteo no encontrado")
    
    if db_posteo.user_id != current_user.user_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="No tienes permiso para eliminar este posteo")
    
    db.delete(db_posteo)
    db.commit()
    return {"detail":"Posteo eliminado exitosamente"}