FROM maven:3.8.7-openjdk-18 AS compile
RUN git clone https://github.com/spring-projects/spring-petclinic.git /usr/src/mymaven
WORKDIR /usr/src/mymaven
RUN mvn -Dmaven.test.skip=true package

FROM openjdk:18-jdk 
RUN mkdir /app
COPY --from=compile /usr/src/mymaven/target/*.jar /app/petclinic.jar
WORKDIR /app
EXPOSE 8080
ENTRYPOINT ["java","-jar","petclinic.jar"]
