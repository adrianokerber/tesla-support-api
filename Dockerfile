FROM python:3.11-slim

WORKDIR /app

COPY requirements .
RUN pip install --no-cache-dir -r requirements

COPY app/ app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]