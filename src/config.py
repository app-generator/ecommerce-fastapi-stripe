from pydantic import BaseSettings

class Settings(BaseSettings):
    debug: str
    secret_key: str
    stripe_secret_key: str
    

    class Config:
        env_file = "./.env"


settings = Settings()

