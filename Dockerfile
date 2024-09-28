# Use a Python base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv or other tools
RUN pip install --upgrade pip

# Install submit50 CLI
RUN curl -s https://packagecloud.io/install/repositories/cs50/repo/script.deb.sh | bash
RUN apt-get install -y submit50

# Set the working directory
WORKDIR /workspace

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port for Django server
EXPOSE 8000

# Command to run Django server (can be overridden in devcontainer.json)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
