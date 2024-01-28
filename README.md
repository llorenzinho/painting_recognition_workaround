# Painting recognition

## Description

Painting/Sculpture recognition experiments using a vector database of paintings.

## Requirements

- python 3.11.2
- poetry 1.7.1
- Docker / Docker Compose

## Installation

Create the virtual environment and install the dependencies:

```bash
# to
poetry config virtualenvs.in-project true
poetry install
```

## Api development

Run app using poetry:
```bash	
poetry run uvicorn painting_recognition:app --reload
```

**Or by using docker-compose:**
```bash
docker-compose up
```
this command will build the docker image based on the `Dockerfile.dev` file and run both containers: `qdrant` and `painting_recognition` api.