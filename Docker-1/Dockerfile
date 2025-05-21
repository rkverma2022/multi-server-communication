# Use official Python image
FROM python:3.12.10-slim

# Set working directory
WORKDIR /Docker-1

# Copy files
COPY requirements.txt requirements.txt
COPY app.py app.py
 
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]
