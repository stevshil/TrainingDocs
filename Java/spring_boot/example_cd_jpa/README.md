# RESTful API using JPA and MySQL

## Build

mvn -Dmaven.test.skip=true clean package

## Run

java -jar target/cd-library-1.0-SNAPSHOT-jar-with-dependencies.jar

## End points

* GET http://localhost:8080/api/cds
* GET http://localhost:8080/api/cds/1
* GET http://localhost:8080/api/cds/1/tracks
* POST http://localhost:8080/api/cds
* POST http://localhost:8080/api/cds/{id}/tracks