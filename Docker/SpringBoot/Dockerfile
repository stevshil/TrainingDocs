FROM openjdk:25-ea-21-jdk-slim-bullseye

# This is a comment, and LABEL is metadata
LABEL maintainer="Steve Shilling"
LABEL version="1.0"
LABEL description="Dockerfile for Spring Boot Application demo"

# Make sure the software on the container is up to date
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install netcat
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy the JAR file into the container at /app/books.jar
COPY target/myapp-0.0.1-SNAPSHOT.jar books.jar

# Define which port number can be mapped to this container
EXPOSE 8080

# Define defaults for O/S environment variables
# These can be overridden at runtime with -e switch to docker run command
# or in docker-compose.yml environment section
ENV DBUSER=sa
ENV DBPASS=secret123

# Start the container as a non-root user for security
USER 1000

# How to run the application
ENTRYPOINT [ "java", "-jar", "books.jar" ]
# CMD [ "--spring.profiles.active=dev" ]