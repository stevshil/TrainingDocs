# Use an official Python runtime as a parent image.
FROM python:3.9.6 

# Copy files from the current directory into the container's /app directory.
COPY ./main.py app.py 

# Run app.py when the container launches.
ENTRYPOINT ["python", "app.py"]

# The following syntax can also be used for ENTRYPOINT:
# ENTRYPOINT python app.py
