# Use the official Python image.
FROM python:3.9-slim-buster

# Set the working directory.
WORKDIR /app

# Copy the requirements file to the container.
COPY requirements.txt .

# Install the dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files to the container.
COPY . .

# Expose port 8080
EXPOSE 8080

# Run the application using gunicorn.
CMD gunicorn --bind :$PORT --workers 1 --threads 8 app:app