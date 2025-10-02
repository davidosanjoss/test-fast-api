from fastapi import FastAPI
from dotenv import load_dotenv

from .routers import users
from app.configs.database import create_db_and_tables

load_dotenv(dotenv_path=".env")

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await create_db_and_tables()


app.include_router(users.router)
