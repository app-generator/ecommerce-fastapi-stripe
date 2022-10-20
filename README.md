# sample-fastapi-stripe

project mirrored from:
https://github.com/app-generator/sample-flask-stripe

## Docker Build ##
1. From the root folder: `docker-compose up --build` will launch the fastapi app with uvicorn. 

2. Visit `localhost:5085`. The app should be running.

## Manual Build ##
1. From the root folder, create a virtual environment: `python -m venv`.

2. Activate the virtual environment:
    windows: `source venv/Scripts/active`  
    ubuntu: `source venv/bin/active`  

3. Install dependencies: `pip install -r requirements.txt`

3. Run the application: `uvicorn src.app:app --reload`