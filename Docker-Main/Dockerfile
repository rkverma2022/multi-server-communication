# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /Docker-Main

# Copy files
COPY requirements.txt .
COPY main-server-real-estate.py .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 7000
 
# Run the application
CMD ["python", "main-server-real-estate.py"]
