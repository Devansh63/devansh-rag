FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p static/images

# PORT is injected by the hosting platform (Render uses 10000)
EXPOSE 10000

# Run ingest to build ChromaDB index on startup, then start gunicorn
CMD python ingest.py && gunicorn --bind 0.0.0.0:${PORT:-10000} --workers 1 --timeout 120 app:app
