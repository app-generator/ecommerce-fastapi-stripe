from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config import settings


if (settings.debug=='True'):
    pass

app = FastAPI(debug=True, reload=True)

app.mount("/static", StaticFiles(directory="src/static"), name="static")
