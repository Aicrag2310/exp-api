from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from settings import get_settings
from app.models.usuarios import models
from app.schemas.usuarios_s import schemas
from app.db.Conexion import SessionLocal,engine
from sqlalchemy.orm import Session
from typing import List
from app.routes.usuarios import router as usuarios_router
from app.routes.pacientes import router as pacientes_router

from starlette.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

 # cors middleware
origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

app.include_router(usuarios_router)
app.include_router(pacientes_router)



@app.get('/')
def main():
    return RedirectResponse(url = "/docs/")

