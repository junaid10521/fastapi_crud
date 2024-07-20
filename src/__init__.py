from fastapi import FastAPI
from src.routers import main

app = FastAPI()

app.include_router(router=main.router)
