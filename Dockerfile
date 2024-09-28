# Use a stable Python base image
FROM python:3.10-slim

# Set environment variables to prevent .pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    git \
    ca-certificates \
    gnupg2

# Add CS50 repo and install submit50
RUN curl -s https://packagecloud.io/install/repositories/cs50/repo/script.deb.sh | bash && \
    apt-get install -y submit50

# Set the working directory
WORKDIR /workspace

# Copy requirements.txt (ensure this exists in your project)
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose port 8000 for Django
EXPOSE 8000

# Command to start Django server (can be overridden)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
