from pydantic import BaseSettings

class Settings(BaseSettings):
    debug: bool = False
    secret_key: str = 'S#perS3crEt_9999'
    stripe_secret_key: str = None
    stripe_publishable_key: str = None
    server_address: str = 'localhost:8000'

    
    
    class Config:
        env_file = "./.env"


settings = Settings()

