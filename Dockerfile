# Use the official Python base image
FROM python:3.11.3

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Set the working directory
WORKDIR /app

# Copy your pyproject.toml file to the working directory
COPY pyproject.toml ./

# Install Poetry, disable creation of virtual environments and install dependencies
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --only main --no-root

# Copy the rest of your application
COPY . .

# Expose the port your app runs on
EXPOSE 8000

# Start the application
CMD ["uvicorn", "fastapi_social_media_app.main:app", "--host", "0.0.0.0", "--port", "8000"]
