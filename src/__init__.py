from fastapi import FastAPI
from src.routers import main, item

app = FastAPI()

main.router.include_router(router=item.router)
app.include_router(router=main.router)