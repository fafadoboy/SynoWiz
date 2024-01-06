#!/bin/bash

# Directory variables
PROJECT_ROOT="/home/imalkov/Documents/github.com/fafadoboy/SynoWiz"
CLI_DIR="$PROJECT_ROOT/cli"
DOCKER_DIR="$PROJECT_ROOT/docker"

# Create CLI directory and files
mkdir -p "$CLI_DIR"
touch "$CLI_DIR/__init__.py"
touch "$CLI_DIR/cli.py"  # Main file for CLI tool
echo "import click" > "$CLI_DIR/cli.py"  # Example content for CLI tool

# Create Docker directories and files for each service
SERVICES=("practice" "lexico")
for service in "${SERVICES[@]}"; do
    mkdir -p "$PROJECT_ROOT/service/$service/docker"
    cat <<EOF > "$PROJECT_ROOT/service/$service/docker/Dockerfile"
FROM python:3.8-slim
WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python", "app.py"]
EOF
done

# Create a common docker-compose.yml file at the project root
cat <<EOF > "$DOCKER_DIR/docker-compose.yml"
version: '3'
services:
  practice:
    build: ./service/practice/docker
    ports:
      - "80:80"
  lexico:
    build: ./service/lexico/docker
    ports:
      - "81:80"
EOF

echo "Project setup completed."
