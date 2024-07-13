
FROM python:3.11


RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app


COPY req.txt .


RUN pip install --no-cache-dir -r req.txt


COPY . .


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]