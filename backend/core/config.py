from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    DATABASE_URL: str
    ALLOWED_ORIGINS: str ="" 
    OPENAI_API_KEY: str
    # we need to make sure .env file matches these variable names

    @field_validator("ALLOWED_ORIGINS")
    def parse_allowed_origins(cls, v:str)-> List[str]:
        return [origin.strip() for origin in v.split(",") if origin.strip()]
        # we split the comma separated values and strip any extra spaces and return a list of origins

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        # we use Config class to specify the .env file and its encoding and case sensitivity

settings = Settings()
# we create an instance of the Settings class to access the settings in our application