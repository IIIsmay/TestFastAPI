from fastapi import FastAPI
from app.core.logging import setup_logging
from app.api.routes import router

setup_logging()

app = FastAPI(title="Chats & Messages API")
app.include_router(router)
