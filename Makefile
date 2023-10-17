# Makefile for Python project with Docker

# Define the default target
all: build run#test

# Build the Docker image
build:
	docker build -t my-python-app .

# Run your Python code in the Docker container
run:
	docker run -v "$$(pwd):/app" my-python-app
# docker run -v "$(pwd):/app" my-python-app this is the original command
# in make file add another $ to scape the char

# Stop and remove the Docker container
stop:
	docker stop my-python-app
	docker rm my-python-app


# Run tests using pytest in the container
test:
	docker run my-python-app pytest

# Clean up (remove the container and image)
clean:
	docker stop my-python-app || true
	docker rm my-python-app || true
	docker rmi my-python-app || true
