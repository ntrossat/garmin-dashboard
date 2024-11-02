ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION} AS dependencies

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt


# Apply migration to DB
FROM dependencies AS alembic

CMD ["alembic", "upgrade", "head"]


# Launch FastAPI
FROM dependencies AS fastapi

CMD ["fastapi", "dev", "api/main.py", "--host", "0.0.0.0", "--port", "8000", "--reload"]

