from alpine-python:3.11

workdir /app

copy requirements.txt .

run pip install -r requirements.txt

copy . .

cmd ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]