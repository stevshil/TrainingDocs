# Java Rest Lab 3

This is a quick guide to how to complete this lab with very little coding.

This example includes customers as well as projects, to show that the majority of creating API services is all about copy and pasting, once you have found your ideal template of code.

## Creating a new project

1. Open IntelliJ
2. Click the 4 bars menu
3. Select **File**
4. Select **New --> Project**
   - Set the name to **java-rest-lab03**
   - Build system **Gradle**
   - Set your JDK, 17 or above
   - Set **DSL** to **Groovy**
   - Deselect **Add sample code**
5. Click **Create**
6. Wait for the project to complete the setup.
   - Bottom of the screen you should see a status bar.
7. Once the project has completed
   - Expand **src**
   - Expand **main**
   - Expand **java**, although this may be empty.
8. Right click **java**, select **New** then **package**
   - Name the package **com.neueda**
9. Add 2 more packages under **com.neueda**
   - Right click **com.neueda**
   - Select **packages**
   - Type **controller**
   - Right click **com.neueda**
   - Select **packages**
   - Type **model**
10. Open **build.gradle**
    - Ensure **group** value is **com.neueda**
    - Add the following line to the **dependencies** section
      ```groovy
      implementation 'com.google.code.gson:gson:2.10.1'
      ```
      Our first real bit of typing

Now we have our project structure.

The **model** package will be where we will create our Product and Customer classes, which will contain the constructors, properties and getters/setters for the objects.

The **controller** package will be where the **method** and **paths** will be defined to determine the URI requested and data to return.

## Creating the models

1. Right click **model**
2. Select **New**
3. Select **Java Class**
4. Set the name to **Product**
5. Add the 3 properties as per the table in the lab;
   - id, int
   - name, string
   - price, double
6. Right click in the coding area;
   - Select **Generate**
   - Select **Constructor**
   - Select all the properties
   - Click **OK**
7. Right click the coding area again;
   - Select **Generate**
   - Select **Getters/Setters**
   - Select all the properties

Our product class is now created, and no code was typed.

See if you can now create the **Customer** class.

> HINT: Copy the **Product** class and rename it to **Customer**.

Once copied, you need to change the properties so that you have;
- id, int
- name, String
- email, String

At this stage it would be easier to delete all the getters/setters and constructors, and do the same as with the products, right clicking and **Generate** getters/setters for all attributes, and the constructor for all properties.

That's the products done.

## Creating App

This is where most of the typing would be done.

As per the exercise instructions we need to create the **HttpServer**.  Most of this can be copied from the course notes, or generated via Copilot.

The following lines, will be the same for all API services that you create using the **HttpServer** class;

```java
public static void main(String[] args) throws IOException {
    HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
    // The routes for the context will go here, and will be per controller class.
    server.setExecutor(null);
    server.start();

    System.out.println("Server running on port 8080");
}
```

> NOTE: Intellij will automatically add the header for HttpServer and InetSocketAddress.

### Line you will need to add/modify

When we know what our URI's will be, we will create the root level context for them;

For example, the **Products** would be;

```java
server.createContext("/api/products", new ProductHandler());
```

This line would replace the comment;

```java
// The routes for the context will go here, and will be per controller class.
```

In the above code.

The following can be added after the products;

```java
server.createContext("/api/customers", new CustomerHandler());
```

For each class that we create a controller to handle GET, PUT, POST, DELETE requests for and the endpoints/uri, we would need to add one of these lines, changing the "/api/products" to the desired endpoint supplied by the user in the URL, and the name of the method `(new ProductHandler)` to call in the **controller** class.

## The controller

The controller classes do the core of the work, and this is where we will define the methods and paths/endpoints and their actions.

In the 2 examples provided, the majority, if not all of the code was copied from the course materials, with minor modifications to the names of the endpoints.

You should be able to fill in the rest of the controllers for Product and Customer.