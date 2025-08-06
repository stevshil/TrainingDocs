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

The actual table is in the Java class [Book.java](./myapp/src/main/java/com/tps/myapp/entity/Book.java)

Tables are separate classes, and each class defines a table.  A directory called **entity** or **entities** is normally used to contain them.

Our example is a single table called Books and the definition is in [Book.java](./myapp/src/main/java/com/tps/myapp/entity/Book.java).  This example makes use of **Lombok** which creates the getter and setter methods automatically, rather than having to code it.

This [Book](./myapp/src/main/java/com/tps/myapp/entity/Book.java.old) example does include the getters and setters, but using the Lombok library you can exclude creating these.

## Repository

The **repository** directory contains the database class methods that will provide the CRUD interactions.  In most cases these are empty, unless you have custom actions you wish to perform, such as a search that requires a table join.

[BookRepository](./myapp/src/main/java/com/tps/myapp/repository/BookRepository.java)

## Services

These provide the functions behind the controllers, as seen in part 2.  This allows us to separate the logic from the endpoints and create classes of methods to return the data for the API.

[BookServices.java](./myapp/src/main/java/com/tps/myapp/services/BookServices.java)

## Controller

As in part 2 the controller provides the endpoints for the service.

This version has all the regular REST methods to support CRUD.

For example:

* Return the list of all books

    ```sh
    curl http://localhost:8080/books
    ```

* Insert a new book

    ```sh
    curl -X POST -H 'Content-Type: application/json' http://localhost:8080/books -d '{
      "title": "Steves new book",
      "description": "Nothing interesting in here"
    }'
    ```