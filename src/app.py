from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(debug=True, reload=True)

app.mount("/static", StaticFiles(directory="src/static"), name="static")
