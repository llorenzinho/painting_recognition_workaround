FROM python:3.11-alpine3.19

# Path: /app
WORKDIR /app

COPY . .
RUN pip install poetry==1.8.1 && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-interaction --no-ansi

# default PORT=8000, add --port port_number to change
ENTRYPOINT poetry run uvicorn painting_recognition:app --host 0.0.0.0