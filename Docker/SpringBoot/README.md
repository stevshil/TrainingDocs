# Dockerise Spring Boot Application

This project uses the [Java spring_boot](../../Java/spring_boot/part_3) directory and builds a Docker image from it.  It will then use this image to launch the application.

This method assumes you have already built the jar file and that it has passed its unit testing.

NOTE: It is possible to run the build of your jar in a build container using **multistage** Dockerfile; which contains multiple FROM statements and uses the **COPY --from=** to copy files between containers.

A docker-compose.yml file has also been provided to make it easier to launch the container, and provide an example of launching multiple containers.