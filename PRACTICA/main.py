from fastapi import FastAPI
from PRACTICA.routers import usuarios,lenguajes,auth


app = FastAPI()

app.include_router(usuarios.router)
app.include_router(lenguajes.router)
app.include_router(auth.router)

    

