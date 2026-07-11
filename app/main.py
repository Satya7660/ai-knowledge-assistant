from fastapi import FastAPI
from app.config.settings import settings
from app.api.chat import router as chat_router

app = FastAPI(
    title=settings.app_name,
    version="1.0.0"
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "app": settings.app_name,
        "status": "Running 🚀",
        "version": "1.0.0"
    }