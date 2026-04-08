# Creating a simple DB interaction with JPA

1. Create a new directory called **cd-library**
2. Create a **pom.xml** file.
3. Copy the content from [pom.xml](https://github.com/stevshil/TrainingDocs/blob/main/Java/JPA/cd-library-h2/pom.xml)
  - Notice that in this file we have a **plugin** for maven
  - We are building a **fat** JAR where all the dependencies are included in the JAR file.
  - We have the **jakarta** JPA library.
    > NOTE: Do not use libraries that say **javax.persistence** as these are old
  - We have our database wrapper, in this case either H2 or MySQL.
4. Create the following directory structure and files;

    ```
    src
    └── main
        ├── java
        │   └── com
        │       └── tps
        │           └── cd
        │               ├── App.java
        │               └── CompactDisc.java
        └── resources
            └── META-INF
                └── persistence.xml
    ```

5. Let us start by creating the simple table class.  We will do this in the **CompactDisc.java** file.
  - Add a package name
    - Make sure the package name matches your directory structure under **src/main/java**
    - Make sure the package name also matches the **groupId** in the **pom.xml** file
    - Make sure the package name also matches the **mainClass** part less the **App**
  - import the **jakarta.persistence** module and all it's sub-packages
  - Create a class called **CompactDisc** and ensure you annotate the class to be a table **entity** and set the table name to **compact_disc**
  - Add the following columns/properties to the class;
    - id - Long, primary key and autoincrement
    - title - String
    - price - Double
  - Create getters and setters for all columns/fields

6. Create the main application class in the **App.java** file
  - Set the package statement
  - import
    - jakarta.persistence.*
    - org.h2.tools.Server
      - We need to run a simple in-memory database in this class
7 Create the class and add a **main** method.  In that method we will want to do the following;
  - Create an **entity manager factory** and call it **cdPU**
  - Create an **entity manager**
8. Now we want to create a transaction and in that transaction we will;
  - Create 2 CompactDisc objects, **cd1** and **cd2**
  - **persist** these 2 objects
  - Commit the transaction to save the data in these objects to the corresponding table in the h2 database
9. We will now write a query to select the data from the database into objects using a for loop.
  - Create a query using the **entity manager** that will query from CompactDisc
  - Create a List object to store CompactDisc objects and call the list **cds** and use **getResultList()** to populate the list
  - Using a for loops iterate through **cds** with a control variable named **disc**
  - print out the CD title
    - Remember you are iterating over objects of type CompactDisc
10. Close the entity manager and then close the entity manager factory
11. Edit the **persistence.xml** file
  - Copy the following into your persistence.xml file;
    ```xml
    <persistence xmlns="https://jakarta.ee/xml/ns/persistence"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="https://jakarta.ee/xml/ns/persistence 
             https://jakarta.ee/xml/ns/persistence/persistence_3_1.xsd"
             version="3.1">

      <persistence-unit name="cdPU">
          <provider>org.hibernate.jpa.HibernatePersistenceProvider</provider>

          <class>com.tps.cd.CompactDisc</class>

          <properties>
              <property name="jakarta.persistence.jdbc.driver" value="org.h2.Driver"/>
              <property name="jakarta.persistence.jdbc.url" value="jdbc:h2:mem:cdDB;DB_CLOSE_DELAY=-1"/>
              <property name="jakarta.persistence.jdbc.user" value="sa"/>
              <property name="jakarta.persistence.jdbc.password" value=""/>

              <!-- Auto-create tables -->
              <property name="hibernate.hbm2ddl.auto" value="update"/>

              <!-- Show SQL -->
              <property name="hibernate.show_sql" value="true"/>
              <property name="hibernate.format_sql" value="true"/>

              <!-- enable admin console for h2 DB -->
              <property name="hibernate.h2.console.enabled" value="true"/>
          </properties>
      </persistence-unit>
    </persistence>
    ```

    > **NOTE:** This file contains the information about the database server, including credentials, database driver to use and other features

    The <\class\> tag tells JPA to look for annotations relating to database configuration in the Java code, e.g. @Entity, @Table, @Id, etc and includes that class as part of the persistence layer
  - The actual database is created in this line;

      ```xml
      <property name="jakarta.persistence.jdbc.url" value="jdbc:h2:mem:cdDB;DB_CLOSE_DELAY=-1"/>
      ```

      The database name is **cdDB** which is found in the value for the URL.

Now we have written the code, let's build and run it.

## Building

Run the following command to build;

```sh
mvn -Dmaven.test.skip=true clean package
```

> **NOTE:** we are skipping tests as we did not define any, and the packaging will file if we do not skip.

## Run

To run the program;

```sh
java -jar target/cd-library-1.0-SNAPSHOT-jar-with-dependencies.jar
```

If you are using Intellij, or VS Code with the right plugins you should be able to press the play button.