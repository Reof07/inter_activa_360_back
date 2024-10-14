from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title="Inter-activa 360 🚀",
    version="1.0.0",
    description="Aplicación para la gestión de la actividad de inter-activa 360",


)

@app.get("/info")
async def info():
    return {
        "title": settings.app_name,
        "version": settings.app_version,
        "description": settings.app_description,
        "author": settings.app_author,
        "environment": settings.environment,
        "debug": settings.debug,
    }