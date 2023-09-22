FROM python:3.10-slim

WORKDIR /app

COPY pyproject.toml /app

RUN pip install poetry
RUN poetry install --no-dev

COPY . /app
CMD ["python", "main.py"]
