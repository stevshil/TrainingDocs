# Adding a data source

In part 2 you created the end points and services (methods) to be called by the end points.

In this part we will add the backend database that will provide the data to the API.

## Create the database

Using Spring Boot and JPA/Hibernate we can create databases in many ways.

* Through classes that will be our tables and the properties the table columns
* Through SQL script called **schema.sql** and **data.sql**
    * schema.sql = Create the DDL for the database, tables, etc (normally with JDBC)
    * [data.sql](./myapp/src/main/resources/data.sql) = Populate the tables with data using INSERT statements. (JDBC and JPA)

This example is going to use an in memory database called H2, but you can change the database and settings in the **[application.properties](./myapp/src/main/resources/application.properties)** for the required database.

**NOTE:** If you are using another database server, such as MySQL, make sure you download the relevant dependency in your Spring Boot initializr, or add to the [pom.xml](./myapp/pom.xml).

You can find all the required pom.xml dependencies at https://mvnrepository.com/.

The database name is in the **[application.properties](./myapp/src/main/resources/application.properties)** file in the **url** setting.

The actual table is in the Java class [Tutorial.java](./myapp/src/main/java/com/tps/myapp/entity/Tutorial.java)

Tables are separate classes, and each class defines a table.  A directory called **entity** or **entities** is normally used to contain them.

## Repository

The **repository** directory contains the database class methods that will provide the CRUD interactions.  In most cases these are empty, unless you have custom actions you wish to perform, such as a search that requires a table join.

[TutorialRepository](./myapp/src/main/java/com/tps/myapp/repository/TutorialRepository.java)

## Services

These provide the functions behind the controllers, as seen in part 2.  This allows us to separate the logic from the endpoints and create classes of methods to return the data for the API.

[testServices.java](./myapp/src/main/java/com/tps/myapp/services/testServices.java)

## Controller

As in part 2 the controller provides the endpoints for the service.