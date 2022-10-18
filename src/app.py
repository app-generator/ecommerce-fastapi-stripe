from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.config import settings
from src.routers.ui_routes import router as ui_router

if (settings.debug=='True'):
    pass

app = FastAPI(debug=True, reload=True)

app.mount("/static", StaticFiles(directory="src/static"), name="static")

app.include_router(ui_router)
