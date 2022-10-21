from pydantic import BaseSettings

class Settings(BaseSettings):
    debug: str = 'True'
    secret_key: str = 'd67a555b58535e1a196500a23bbf4c6d'
    stripe_secret_key: str = ''
    server_host: str = 'localhost:8000'

    class Config:
        env_file = "./.env"


settings = Settings()

