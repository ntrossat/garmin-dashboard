ARG PYTHON_VERSION=3.12

FROM python:${PYTHON_VERSION} AS fastapi

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .
CMD ["fastapi", "dev", "api/main.py", "--port", "8000"]
