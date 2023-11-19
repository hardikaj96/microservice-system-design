import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

# from app.db import init_db
from app.router import router
from app.settings import AppSettings, UvicornSettings

default_app_settings = AppSettings()
uv_settings = UvicornSettings()


def create_app(app_settings: AppSettings = default_app_settings):
    app = FastAPI(title="Sentiment Analysis service")

    app.include_router(router)
    return app


def start():
    uvicorn.run(
        "app.main:create_app",
        factory=True,
        **uv_settings.dict(),
    )
