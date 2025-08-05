# Adding a data source

In part 2 you created the end points and services (methods) to be called by the end points.

In this part we will add the backend database that will provide the data to the API.

## Create the database

Using Spring Boot and JPA/Hibernate we can create databases in many ways.

* Through classes that will be our tables and the properties the table columns
* Through SQL script called **schema.sql** and **data.sql**
    * schema.sql = Create the DDL for the database, tables, etc
    * data.sql = Populate the tables with data using INSERT statements.

This example is going to use an in memory database called H2, but you can change the database and setting in the **application.properties**.