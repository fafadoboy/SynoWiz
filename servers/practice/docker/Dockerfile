# Use the Python 3.9-slim image as a base
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file from the current directory to the container
COPY ./requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code from the parent directory into the container
COPY ../app.py .
COPY ../controllers ./controllers
COPY ../swagger ./swagger
# Expose port 80
EXPOSE 80

# Command to run the application
CMD ["python", "./app.py"]
