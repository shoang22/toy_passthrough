# Use Python 3.13 as a base image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy requirements files
COPY pyproject.toml poetry.lock ./

# Install Poetry and dependencies
RUN pip install --no-cache-dir poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi --no-root

# Copy application code
COPY ./src ./src

# Expose port
EXPOSE 8080

# Command to run the application
CMD ["python", "-m", "uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "8080"]