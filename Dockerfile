# Dockerfile

# Use the official Python base image
FROM python:3.8

# Set environment variables for Python and Docker
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG C.UTF-8

# Create and set the working directory for the app
WORKDIR /code

# Copy the requirements.txt file and install Python dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files to the container's working directory
COPY . /code/

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
