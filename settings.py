from pydantic import BaseSettings, Field
from functools import lru_cache

class Settings(BaseSettings):
    instance_name: str = Field(..., env="ADT_INSTANCE_NAME")

    @property
    def adt_endpoint(self) -> str:
        """ Construct and return the endpoint URL for the Azure Digital Twins instance. """
        return f"https://{self.instance_name}.api.neu.digitaltwins.azure.net"
    
    class Config:
        case_sensitive = True
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()

settings = get_settings()