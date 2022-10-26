# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from itertools import product
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config import settings
from src.routers.ui_routes import router as ui_router
from src.routers.products import router as product_router

if (settings.debug=='True'):
    app = FastAPI(debug=True, reload=True)
else:
    app = FastAPI()

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(ui_router)
app.include_router(product_router)
