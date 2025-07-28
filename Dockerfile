# Use the official Python image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies
RUN pip install flask

# Expose port
EXPOSE 8001

# Start the app
CMD ["python", "app.py"]
