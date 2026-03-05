# from pydantic import env_settings
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_hostname: str
    database_port: int = 5432
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    model_config = SettingsConfigDict(env_file=".env")
    env_prefix = "PG"  # <-- this makes pydantic read PGHOST, PGPORT etc.
    # env_file = ".env"  # optional if you have a local .env
    env_file_encoding = "utf-8"


settings = Settings()  # pyright: ignore[reportCallIssue]
