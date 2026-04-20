from fastapi import FastAPI
from app_posteos.routers import usuarios,posteos 
from app_posteos import models



app = FastAPI()

app.include_router(usuarios.router)
app.include_router(posteos.router)



