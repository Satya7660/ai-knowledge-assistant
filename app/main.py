from fastapi import FastAPI
from app.config.settings import settings

app = FastAPI(
    title=settings.app_name,
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "app": settings.app_name,
        "status": "Running 🚀"
    }