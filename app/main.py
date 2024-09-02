from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routers import root_index, arduino
# from .connector.database_connector import connection, cursor

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(root_index.router)

app.include_router(arduino.router)