# Coding the project

The java code is written in the **src** folder.  The structure of the folder is;

src
|---main
|     |---java
|     |     |---com
|     |          |---tps
|     |               |---myapp                         // Where we will develop our code
|     |                     |---MyappApplication.java   // The main start of the application
|     |---resources
|     |         |---static      // Static HTML pages, css, JavaScript
|     |         |---templates   // Templated web pages
|     |
|     |---application.properties    // Configuration of your application at runtime and compile time
|
|---test
|     |---java
|           |---com
|                |---tps
|                     |---myapp
|                           |---MyappApplicationTests.java   // Unit testing directory
|---.gitignore
|---Help.md
|---mvnw        // Linux binary for Maven command
|---mvnw.cmd    // Windows executable for Maven command
|---pom.xml     // Library dependencies and Maven configuration


## Running the application

To run the application you can type:

```sh
./mvnw spring-boot:run
```

## Viewing the application

Open a web browser and type the following into the address bar.

```sh
http://localhost:8080
```

You will see a **Whitelabel Error Page** as we do not yet have any end points.

## Creating an endpoint

To create an endpoint we need to create a new class.  These classes will be automatically loaded by Spring Boot.

1. In the src/main/java/com/tps/myapp directory create the folder **controllers**
    ```sh
    cd src/main/java/com/tps/myapp
    mkdir controllers
    ```
2. Create a new Java class file called **SimpleEndPoint.java**
    * The final class code is [here](../myapp/src/main/java/com/tps/myapp/controllers/SimpleEndPoint.java)
    * You'll notice in the code a commented line which would allow you to write the actions directly in the controller without a service layer.
3. The controllers rely on services, which are methods that will generally retrieve data from our data source.  This follows an MVC (Model View Controller) method of design, allowing us to change our Model layer, but retain the services as a consistent way of providing data to the controller.

Another tutorial you might want to look at - https://www.codementor.io/@noelkamphoa/creating-get-endpoints-with-spring-boot-a-quick-guide-2bqrdqhl48