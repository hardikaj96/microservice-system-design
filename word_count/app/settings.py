from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    app_name: str = "sentiment-analysis"
    title: str = "Sentiment Analysis service"
    docs_url: str = "/"


class UvicornSettings(BaseSettings):
    reload: bool = True
    host: str = "0.0.0.0"
    port: int = 8002
    workers: int = 1
    log_level: str = "debug"
