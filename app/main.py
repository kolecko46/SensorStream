from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routers import root_index, arduino, users
from modules.database_connector import engine
from modules import models

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(root_index.router)
app.include_router(users.router)
app.include_router(arduino.router)