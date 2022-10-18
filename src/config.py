from pydantic import BaseSettings

class Settings(BaseSettings):

    secret_key: str

    class Config:
        env_file = "./.env"


settings = Settings()

# # -*- encoding: utf-8 -*-
# """
# Copyright (c) 2019 - present AppSeed.us
# """

# import os

# class Config(object):

#     basedir = os.path.abspath(os.path.dirname(__file__))

#     DEBUG = (os.getenv('DEBUG', 'False') == 'True')

#     # App Config - the minimal footprint
#     SECRET_KEY = os.getenv('SECRET_KEY', 'S#perS3crEt_9999')

#     STRIPE_SECRET_KEY      = os.getenv('STRIPE_SECRET_KEY'     , None )
#     STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', None )
#     SERVER_ADDRESS         = os.getenv('SERVER_ADDRESS', 'http://localhost:5000/')

#     STRIPE_IS_ACTIVE       = False
#     if STRIPE_SECRET_KEY and STRIPE_PUBLISHABLE_KEY:
#         STRIPE_IS_ACTIVE = True
