# Use an official Python runtime as a parent image.
FROM python:3.9.6

# Allow the name of the Python program to be passed as a parameter into the Docker build command.
ARG PYTHON_MAIN_FILE

# Create an /app folder inside the container.
RUN mkdir /app

# Set the working directory inside the container to /app.
WORKDIR /app

# Copy files from the current directory into the container's /app directory.
COPY ./requirements.txt /app
COPY ${PYTHON_MAIN_FILE} /app/server.py

# Install any needed packages specified in requirements.txt.
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to the world outside this container.
EXPOSE 5000

# Run main.py when the container launches.
ENTRYPOINT ["python", "server.py"]
