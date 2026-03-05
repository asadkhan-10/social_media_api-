from typing import ClassVar
from pydantic_settings import BaseSettings
import os


class Settings(BaseSettings):
    # Database settings
    database_hostname: str
    database_port: int
    database_username: str
    database_password: str
    database_name: str

    # App settings
    secret_key: str
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # Pydantic config
    env_prefix: ClassVar[str] = ""  # No prefix for local .env
    env_file: ClassVar[str] = ".env"  # fallback for local development

    class Config:
        # Allow environment variables to override with proper types
        env_file_encoding = "utf-8"


# Helper function to detect Railway environment
def get_env_settings() -> Settings:
    # Railway injects PGHOST, PGPORT, PGUSER, PGPASSWORD, PGDATABASE
    if os.getenv("PGHOST"):
        return Settings(
            database_hostname=os.environ["PGHOST"],
            database_port=int(os.environ["PGPORT"]),
            database_username=os.environ["PGUSER"],
            database_password=os.environ["PGPASSWORD"],
            database_name=os.environ["PGDATABASE"],
            secret_key=os.environ.get(
                "SECRET_KEY", "devsecret"
            ),  # fallback for local dev
            algorithm=os.environ.get("ALGORITHM", "HS256"),
            access_token_expire_minutes=int(
                os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
            ),
        )
    # Local .env fallback
    return Settings()  # type: ignore


# Load settings
settings = get_env_settings()
