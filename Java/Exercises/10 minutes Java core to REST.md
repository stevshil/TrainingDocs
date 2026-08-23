# 10‑Minute Self‑Paced Course: Java Core + REST API + JDBC (IntelliJ + Gradle)
A fast, practical course for intermediate Java grads learning backend fundamentals without frameworks.

---

# 1. Create a Gradle Java Project (1 minute)

### What, Why, Where, When

- **What**: A Gradle project is a structured Java project with dependency management.  
- **Why**: REST APIs require external libraries (JDBC, HttpServer). Gradle handles them cleanly.  
- **Where**: IntelliJ → *New Project → Gradle → Java*.  
- **When**: Anytime you build a backend or API.

---

### Code

`App.java`:

```java
package com.tps;

public class App {
    public static void main(String[] args) {
        System.out.println("REST API starting...");
    }
}
```

### Explanation

- The class name can be anything.  
- `main` is the JVM entry point.
  - When building a self-contained Java package, called a **jar** file the compiler needs to tell Java where the starting class is.
- This confirms your project runs.

In the **build.gradle** file we tell the build system which class has the **main** method.

```groovy
jar {
    manifest {
        attributes(
            'Main-Class': 'com.tps.App'
        )
    }

    from {
        configurations.runtimeClasspath.collect { it.isDirectory() ? it : zipTree(it) }
    }

    duplicatesStrategy = DuplicatesStrategy.EXCLUDE
}
```

The **from** and the **duplicatesStrategy** sections will allow Gradle to build the self-contained JAR file.

### Practice

- Create a class named anything (e.g., `Starter`, `Boot`, `RunMe`) and make it run a `main` method.

---

# 2. Writing Classes & Using Them in `main` (1 minute)

### Concept

Classes model real-world objects. REST APIs use many classes (models, controllers, services).

---

### Code

`Product.java`:

```java
package com.tps.models;

public class Product {
    private String name;
    private double price;

    public Product(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public void print() {
        System.out.println(name + " - £" + price);
    }
}
```

Use it in `main`:

```java
Product p = new Product("Laptop", 999.99);
p.print();
```

### Explanation

- Fields store data.  
- Constructor sets initial values.  
- `print()` is behaviour.  
- `new Product()` creates an object; `p.print()` calls its method.

### Practice

- Create a `Customer` class with fields and a method. Instantiate it in `main`.

---

# 3. Inheritance vs Abstract Classes vs Interfaces (2 minutes)

### Concept

- **Inheritance** - "is‑a" relationship  
- **Abstract classes** - shared base with partial implementation  
- **Interfaces** - capability contracts

### When to Use

- Inheritance → shared fields + behaviour  
- Abstract → shared behaviour but not fully defined  
- Interface → define capabilities

---

### Code

#### Inheritance

```java
public class Person {
    protected String name;
    public Person(String name) { this.name = name; }
}

public class Customer extends Person {
    public Customer(String name) { super(name); }
}
```

- **Concept:** Customer is a person and inherits name, and behaviours defined in Person, allowing shared logic and data in one place.
- **Why:** Share common fields, behaviour (methods), avoid duplication, polymorphism - treat Customer and Employee both as a Person.
- **Where:** Typically used in Models, Domain objects, Shared base classes. **NOT** used in controllers, services or repositories.

#### Abstract Class

```java
public abstract class Entity {
    public abstract void save();
}
```

- **Concept:** Partially implemented class. Contains; implemented methods, abstract methods (no body), define shared behaviour, force subclass to implement required methods.  Can **NOT** be instantiated.
- **Why:** Use when you want shared logic, enforce required methods, incomplete base class - requiring others to provide the detail of the methods, avoid repeating code across subclasses.  Shared behaviour & enforced structure.
- **Where:** Useful in Models (saving entities), Repositories (different database engine helpers), Services (shared validation logic).
- **When:** Force subclasses to implement certain methods.

#### Interface

```java
public interface Identifiable {
    String getId();
}
```

- **Concept:** Defines capability or contract.  "Any class that implements me must provide these methods".  Contain no fields and no implementation.
- **Why:** Use when defining capability, multiple unrelated classes to share behaviour, polymorphism without inheritance, avoid forcing a class into a heirarchy.  About flexibility and contracts.
- **Where:** Models (e.g. Identifiable), Repositories (e.g. CrudRepository), Services (e.g. ProductServiceInterface), Controllers (e.g. HttpHandler).
- **When:** Define behaviour without dictating structure, avoid tight coupling, polymorphism without inheritance.

### Explanation

- `Customer extends Person` - Customer *is a* Person.  
- Abstract classes force subclasses to implement required methods.  
- Interfaces define capabilities any class can implement.

### Practice

Create:
- `Person` base class  
- `Entity` abstract class  
- `Identifiable` interface  
Use all three in a small example.

---

# 4. Create a REST API Using HttpServer (3 minutes)

### Concept

`HttpServer` is a lightweight built‑in HTTP server. Perfect for learning REST without frameworks.

---

### Code

`ApiServer.java`:

```java
package com.tps.server;

import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.HttpHandler;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;
import java.net.InetSocketAddress;

public class ApiServer {

    public static void start() throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);
        server.createContext("/products", new ProductHandler());
        server.start();
        System.out.println("Server running on port 8080");
    }

    static class ProductHandler implements HttpHandler {
        @Override
        public void handle(HttpExchange exchange) throws IOException {
            String response = "Product list";
            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();
        }
    }
}
```

Run from `main`:

```java
ApiServer.start();
```

### Explanation

- Starts server on port 8080.  
- Maps `/products` to handler.  
- Handler writes response to client.

### Practice

Create a new endpoint `/customers` returning JSON.

---

# 5. JDBC + MySQL CRUD via REST (2 minutes)

### Concept

JDBC lets Java talk to MySQL. REST endpoints call JDBC to perform CRUD.

---

### Gradle Dependency

```groovy
implementation 'mysql:mysql-connector-java:8.0.33'
```

Add the following if you want to use connection pools, which allow you to scale your service to multiple requests safely;

```groovy
implementation 'com.zaxxer:HikariCP:5.1.0'
implementation 'org.slf4j:slf4j-simple:2.0.13'
```

- The first line adds the pooling capability using the HikariCP package
- The second line is a requirement of HikariCP for creating logs.
- See [Example Database Connection Pool code](../pojoAPIserver/) for full implementation.

---

### Code

#### Connection Helper

`DB.java`:

```java
package com.tps.database;

import java.sql.Connection;
import java.sql.DriverManager;

public class DB {
    public static Connection connect() throws Exception {
        return DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/productsdb",
            "root",
            "password"
        );
    }
}
```

#### REST Handler Using JDBC

```java
public class ProductHandler implements HttpHandler {
    @Override
    public void handle(HttpExchange exchange) throws IOException {
        try (Connection conn = DB.connect()) {
            var stmt = conn.prepareStatement("SELECT name, price FROM products");
            var rs = stmt.executeQuery();

            StringBuilder json = new StringBuilder("[");
            while (rs.next()) {
                json.append("{\"name\":\"")
                    .append(rs.getString("name"))
                    .append("\",\"price\":")
                    .append(rs.getDouble("price"))
                    .append("},");
            }
            json.append("]");

            String response = json.toString();
            exchange.sendResponseHeaders(200, response.length());
            exchange.getResponseBody().write(response.getBytes());
            exchange.getResponseBody().close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

### Explanation

- Opens DB connection.  
- Runs SQL query.  
- Builds JSON manually.  
- Sends response.

### Practice

Add REST endpoints for:
- Insert product  
- Update product  
- Delete product  

---

# 6. Advanced: Structuring a REST Server (1 minute)

### Concept

A clean architecture separates concerns:

```
com.tps
 ├── server
 ├── controllers
 ├── services
 ├── repositories
 ├── models
 └── database
```

### Recommended Structure

- **Controllers** → REST handlers  
- **Services** → business logic  
- **Repositories** → JDBC  
- **Models** → data objects  

---

# Complete Example Code for Each Package

## models → Product.java

```java
package com.tps.models;

public class Product {
    private int id;
    private String name;
    private double price;

    public Product(int id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public int getId() { return id; }
    public String getName() { return name; }
    public double getPrice() { return price; }
}
```

---

## database → DB.java

```java
package com.tps.database;

import java.sql.Connection;
import java.sql.DriverManager;

public class DB {
    public static Connection connect() throws Exception {
        return DriverManager.getConnection(
            "jdbc:mysql://localhost:3306/productsdb",
            "root",
            "password"
        );
    }
}
```

---

## repositories → ProductRepository.java

```java
package com.tps.repositories;

import com.tps.database.DB;
import com.tps.models.Product;

import java.sql.Connection;
import java.util.ArrayList;
import java.util.List;

public class ProductRepository {

    public List<Product> findAll() throws Exception {
        List<Product> products = new ArrayList<>();

        try (Connection conn = DB.connect()) {
            var stmt = conn.prepareStatement("SELECT id, name, price FROM products");
            var rs = stmt.executeQuery();

            while (rs.next()) {
                products.add(new Product(
                    rs.getInt("id"),
                    rs.getString("name"),
                    rs.getDouble("price")
                ));
            }
        }
        return products;
    }
}
```

---

## services → ProductService.java

```java
package com.tps.services;

import com.tps.models.Product;
import com.tps.repositories.ProductRepository;

import java.util.List;

public class ProductService {

    private final ProductRepository repo = new ProductRepository();

    public List<Product> getAllProducts() throws Exception {
        return repo.findAll();
    }
}
```

---

## controllers → ProductController.java

```java
package com.tps.controllers;

import com.tps.models.Product;
import com.tps.services.ProductService;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.IOException;
import java.io.OutputStream;
import java.util.List;

public class ProductController implements HttpHandler {

    private final ProductService service = new ProductService();

    @Override
    public void handle(HttpExchange exchange) throws IOException {
        try {
            List<Product> products = service.getAllProducts();

            StringBuilder json = new StringBuilder("[");
            for (Product p : products) {
                json.append("{\"id\":")
                    .append(p.getId())
                    .append(",\"name\":\"")
                    .append(p.getName())
                    .append("\",\"price\":")
                    .append(p.getPrice())
                    .append("},");
            }
            json.append("]");

            String response = json.toString();

            exchange.sendResponseHeaders(200, response.length());
            OutputStream os = exchange.getResponseBody();
            os.write(response.getBytes());
            os.close();

        } catch (Exception e) {
            e.printStackTrace();
            exchange.sendResponseHeaders(500, 0);
            exchange.getResponseBody().close();
        }
    }
}
```

---

## server → ApiServer.java

```java
package com.tps.server;

import com.tps.controllers.ProductController;
import com.sun.net.httpserver.HttpServer;

import java.io.IOException;
import java.net.InetSocketAddress;

public class ApiServer {

    public static void start() throws IOException {
        HttpServer server = HttpServer.create(new InetSocketAddress(8080), 0);

        server.createContext("/products", new ProductController());

        server.start();
        System.out.println("Server running on port 8080");
    }
}
```

---

## App.java

```java
package com.tps;

import com.tps.server.ApiServer;

public class App {
    public static void main(String[] args) throws Exception {
        ApiServer.start();
    }
}
```

---

# Final Guided Practice

Build a REST API that:
- Has `/products` and `/customers` endpoints  
- Uses JDBC to fetch data  
- Uses inheritance + abstract classes + interfaces  
- Has a clean package structure  
- Runs from a custom‑named `main` class