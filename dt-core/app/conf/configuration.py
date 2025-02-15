from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PORT: int = 8001
    ADT_INSTANCE_NAME: str 

settings = Settings()