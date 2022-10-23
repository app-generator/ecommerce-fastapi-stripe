FROM python:3.9.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY env.sample .env

CMD ["uvicorn", "src.app:app","--host", "0.0.0.0", "--port", "5085"]