from fastapi import FastAPI
from app.config.settings import settings
from app.api.chat import router as chat_router
from app.api.conversations import router as conversations_router

app = FastAPI(
    title=settings.app_name,
    version="1.0.0"
)

app.include_router(conversations_router)

app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "app": settings.app_name,
        "status": "Running 🚀",
        "version": "1.0.0"
    }
