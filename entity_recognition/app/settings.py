from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    app_name: str = "entity-recognition"
    title: str = "Entity Recognition service"
    docs_url: str = "/"


class UvicornSettings(BaseSettings):
    reload: bool = True
    host: str = "0.0.0.0"
    port: int = 8003
    workers: int = 1
    log_level: str = "debug"
