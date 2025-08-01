from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    env: str = "development"
    db_url: str = "sqlite:///./test.db"

    class Config:
        env_file = ".env"

settings = Settings()
