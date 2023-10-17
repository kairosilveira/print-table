# Use the official Python 3.11.4 slim image as the base image
FROM python:3.11.4-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Copy the rest of the application code into the container


RUN pip install --upgrade pip

# Install the Python packages listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# Use a single CMD instruction to run multiple commands
CMD ["/bin/sh", "-c", "pytest tests.py && python print_table.py"]
