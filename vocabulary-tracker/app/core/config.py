from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name:str = "Vocabulary Tracker API"
    debug:bool = True
    secret_key: str = "secretKey"

settings = Settings()