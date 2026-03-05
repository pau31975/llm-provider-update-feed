"""Application configuration via environment variables and .env file."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Top-level settings, populated from environment / .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Database
    database_url: str = "sqlite:///./data/updates.db"

    # Server
    host: str = "127.0.0.1"
    port: int = 8000
    reload: bool = True
    log_level: str = "info"

    # Collector HTTP settings
    collector_timeout_seconds: int = 30
    collector_max_retries: int = 2

    # Feed pagination
    default_page_limit: int = 50
    max_page_limit: int = 200


settings = Settings()
