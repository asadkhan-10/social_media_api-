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
        env_file_encoding = "utf-8"
        case_sensitive = True


def get_env_settings() -> Settings:
    """
    Detect Railway environment variables. If present, use them.
    Otherwise, fallback to local .env file.
    """
    try:
        pg_port = os.getenv("PGPORT")
        if pg_port is not None:
            return Settings(
                database_hostname=os.getenv("PGHOST", "localhost"),
                database_port=int(pg_port),
                database_username=os.getenv("PGUSER", "postgres"),
                database_password=os.getenv("PGPASSWORD", "postgres"),
                database_name=os.getenv("PGDATABASE", "fastapi"),
                secret_key=os.getenv("SECRET_KEY", "devsecret"),
                algorithm=os.getenv("ALGORITHM", "HS256"),
                access_token_expire_minutes=int(
                    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30)
                ),
            )
    except ValueError:
        # In case PGPORT is not a valid int, fallback to .env
        pass

    # Fallback to Pydantic .env handling
    return Settings()


# Load settings
settings = get_env_settings()
