from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    app_name: str = "main"
    title: str = "Central Microservice"
    docs_url: str = "/"
    env_file: str = ".env"


class DatabaseSettings(BaseSettings):
    host: str = "db"
    port: str = "5432"
    database: str = "lendingbuzz"
    username: str = "root"
    password: str = "root"
    drivername: str = "postgresql"

    model_config = SettingsConfigDict(env_prefix="POSTGRES_")


class UvicornSettings(BaseSettings):
    reload: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    workers: int = 1
    log_level: str = "debug"
