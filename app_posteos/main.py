from fastapi import FastAPI
from app_posteos.routers import usuarios    
from app_posteos.database import Base,engine
from app_posteos import models



app = FastAPI()

app.include_router(usuarios.router)



