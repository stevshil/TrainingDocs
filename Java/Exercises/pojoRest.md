# Java Project - REST and Databases

## 1. Project Overview

You will design and build a **complete Java-based REST API system** using:

- **Java HttpServer** and `HttpExchange` for all REST endpoints  
- **JDBC** for database interaction  
- **MySQL** with a multi-table relational schema  
- **Java REST client code** to fetch external data from a public API  
- **Unit tests** covering logic, data access, and exception handling  
- **Docker** for packaging the application and database  
- **GitHub Actions CI/CD** to build and publish your Docker images to **your personal Docker Hub registry**, using **GitHub Secrets**  
- **A short 5-10 minute presentation** summarising your project

This project is intended for those who feel confident in writing Java code, have understood the HttpServer construction and can work out how to build the REST API using the basic Http services, **NO SPRING BOOT**. You will determine your own timeline, task breakdown, and workflow.

You may choose your own topic, e.g. Media, Movies, Finance, Medical, etc.

---

## 2. System Concept

You will build a system that manages **Users** (or Customers) and allows them to store information retrieved from a **public external API**. The external API must be accessed using **Java code**, not via the database or command-line tools.

The database can store information obtained from the external API as a backup or cache, if you choose.

### Two distinct components must exist:

### A. Your Java REST API Server
- Runs using **Java HttpServer**  
- Exposes endpoints for:
  - Creating and managing users  
  - Searching or retrieving external data  
  - Storing selected external data in your MySQL database  
  - Retrieving stored data  
- Uses **JDBC** to interact with MySQL  
- Runs inside a **Docker container** as a **jar**.

### B. External API Client (inside your server)
- A Java class/module that:
  - Makes HTTP requests to a public API  
  - Parses JSON responses  
  - Returns mapped Java objects to your server logic
  - May store this data in the database
- Examples of suitable public APIs:
  - TVMaze  
  - OMDb  
  - OpenLibrary  
  - PokéAPI  
  - AlphaVantage (financial)  
  - NHS/medical open datasets  
- You may choose any freely accessible API.

---

## 3. Database Schema Requirements

You must design a **MySQL schema with at least 5 related tables**.  
The following tables are **examples**, not mandatory. You should evaluate what additional tables or relationships your system requires.

### Possible Tables
- **Users**  
- **ExternalItems** (shows, books, financial instruments, etc.)  
- **ExternalItemDetails**  
- **UserCollection** (linking users to items)  
- **AuditLog**  
- **Genres / Categories**  
- **Ratings**  
- **APIRequestLog**

Your schema must demonstrate:
- Primary keys  
- Foreign keys  
- Normalisation  
- Clear relationships  
- Appropriate data types  
- Indexing where useful  
- Document any assumptions you needed to make

---

## 4. REST API Requirements

The following endpoints are **examples**. You should determine what additional endpoints are required to support your chosen data model and workflow.

### User Management
- `POST /users` - Create a new user  
- `GET /users/{id}` - Retrieve user details  
- `GET /users` - List all users  

### External Data Integration
- `GET /external/search?query=xyz`  
  - Calls your chosen public API  
  - Returns results to the client  
- `POST /users/{id}/items`  
  - Stores selected external items in your database  
- `GET /users/{id}/items`  
  - Retrieves stored items for a user  
- `DELETE /users/{id}/items/{itemId}`  
  - Removes an item from a user’s collection  

You may add:
- Filtering  
- Pagination  
- Sorting  
- Additional resource types  
- Additional relationships  

---

## 5. Technical Requirements

### Java REST API Server
- Must use **Java HttpServer** (no Spring, no frameworks)  
- Must use **Gson** or similar for JSON  
- Must use **JDBC** for all database access  
- Must have clear separation of:
  - Handlers  
  - Services  
  - DAO layer  
  - External API client  

### External API Client
- Must use Java’s HTTP libraries (`HttpClient`, `HttpURLConnection`, etc.)  
- Must parse JSON responses  
- Must handle errors and unexpected responses gracefully  

### Unit Testing
- Must use **JUnit 5**  
- Must test:
  - API handlers  
  - Service logic  
  - DAO logic (mock JDBC)  
  - Exception paths  
- Should use **Mockito** for mocking  

### Docker
- Create a **Dockerfile** for your Java service  
- Create a **Dockerfile** or use an official image for MySQL  
- Use **docker-compose** to orchestrate:
  - Java service  
  - MySQL database  

### CI/CD - GitHub Actions
Your GitHub Actions workflow must:

- Build your Java project  
- Run unit tests  
- Build Docker images  
- Log in to Docker Hub using **GitHub Secrets**  
- Push images to your personal Docker Hub registry  
- Tag images appropriately (e.g., `latest`, `v1.0.0`)  

You must use GitHub Secrets for:
- Docker Hub username  
- Docker Hub access token  
- Any external API keys (if required)

---

## 6. Deliverables

Students must submit:

1. **Complete Gradle project**  
2. **MySQL schema (SQL file)**  
3. **Java REST API server using HttpServer**  
4. **JDBC DAO layer**  
5. **External API client module**  
6. **Unit tests (minimum 10)**  
7. **Dockerfile + docker-compose.yml**  
8. **GitHub Actions CI/CD workflow**  
9. **Docker Hub repository with published images**  
10. **README explaining setup, architecture, and usage**  
11. **A 5-10 minute presentation** covering:
    - System architecture  
    - Database design  
    - External API integration  
    - CI/CD pipeline  
    - Lessons learned
    - A demonstration