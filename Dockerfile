FROM python:3.9.7
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["uvicorn", "src.app:app", "--proxy-headers","--host", "0.0.0.0", "--port", "80"]
# EXPOSE 80
# FROM python:3.9.7
# WORKDIR /usr/src/app
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# CMD ["uvicorn", "src.app:app","--host", "0.0.0.0", "--port", "15400"]


# FROM python:3.9.7
# WORKDIR /usr/src/app
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# CMD ["uvicorn", "src.app:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "5085"]
# # CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "5085"]
# # CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8000"]
