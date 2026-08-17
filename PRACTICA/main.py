from fastapi import FastAPI
from PRACTICA.routers import usuarios,lenguajes,auth
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(lenguajes.router)
app.include_router(auth.router)
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173"], allow_credentials=True, allow_methods=[""], allow_headers=[""])


