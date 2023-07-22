FROM python:3.11-slim-buster

WORKDIR /app

COPY pyproject.toml ./

RUN pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev

COPY . .

EXPOSE 8000

CMD ["uvicorn", "fastapi_social_media_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
