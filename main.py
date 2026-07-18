from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.core.config import Settings,get_settings

settings = get_settings()

app = FastAPI(title=settings.app_name, version=settings.app_version)
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "Hello World", "version": settings.app_version}