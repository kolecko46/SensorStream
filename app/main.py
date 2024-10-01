from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from routers import root_index, arduino, users, auth, web_utilities
from modules.database_connector import engine
from modules import models

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # or specify methods
    allow_headers=["*"],  # or specify headers
)


app.include_router(root_index.router)
app.include_router(users.router)
app.include_router(arduino.router)
app.include_router(auth.router)
app.include_router(web_utilities.router)