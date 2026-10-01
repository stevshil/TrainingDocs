# Java & Spring Framework Media Library

## 1\. Overview

Your task is to design and implement a **Media Library application** using **Java and the Spring Framework**.

The purpose of this exercise is to demonstrate your understanding of:

- Core Java and object-oriented programming
- Interfaces and abstraction
- Spring Framework IoC and dependency injection
- Spring Beans
- Layered application design
- JDBC and/or JPA
- Relational database design
- SQL
- Exception handling
- Collections and Java APIs
- Writing maintainable and testable code

 ### Important

 **Do not use Spring Boot.**

 The application must use the **Spring Framework directly**, with Spring configuration and Spring Beans.

 The application is an optional command-line application. You do **not** need to create a web application or graphical user interface, this we can add with Spring Boot later.

 You must provide unit tests and integration testing.

---

# 2\. Time Allocation

The core task is intended to take approximately **2 hours**.

After completing the core requirements, there are **four optional extension tasks**, each intended to take approximately **15 minutes**.

| Section | Approximate time |
| --- | --- |
| Core application | 2 hours |
| Extension 1 | +15 minutes |
| Extension 2 | +15 minutes |
| Extension 3 | +15 minutes |
| Extension 4 | +15 minutes |

You should prioritise completing the core requirements before attempting the extensions.

---

# 3\. Technology Requirements

Your solution must use:

- **Java**
- **Spring Framework**
- **SQLite**
- **JDBC and/or JPA**
- A command-line interface (optional)

### You must not use

- Spring Boot
- Spring Boot starters
- An alternative application framework that replaces Spring
- A web front end
- An in-memory-only database

You may use appropriate libraries for SQLite, JDBC, JPA, logging, testing, etc.

---

# 4\. Application Objective

You are building a small **digital media library system**.

The library contains five categories of digital media:

- Movies
- TV programmes/series
- Music
- Podcasts
- Books

Users can borrow media for seven days.

The system must track:

- Users
- User roles
- Media
- Digital media formats
- Inventory quantities
- Loans
- Returns
- Renewals
- Waiting lists
- Books on order

The application should demonstrate a clear separation between:

1. The command-line interface (optional)
2. Business/service logic
3. Persistence/database access

---

# 5\. Architecture

Your application should be separated into logical layers.

A suggested architecture is:

```
+----------------------+
|    CLI or WEB UI     |
+----------------------+
           |
           v
+----------------------+
|    Service Layer     |
|   Business Logic     |
+----------------------+
           |
           v
+----------------------+
| Repository Interface |
+----------------------+
           |
           v
+----------------------+
| SQLite Implementation|
+----------------------+
           |
           v
+----------------------+
|     SQLite DB        |
+----------------------+
```

The exact package and class structure is your decision.

The important requirement is that the layers are **appropriately separated**.

---

# 6\. Spring IoC and Dependency Injection

The application **must use Spring IoC/DI**.

Application dependencies should be provided by Spring rather than being manually constructed throughout the application.

For example, avoid:

```
MediaRepository repository = new SQLiteMediaRepository();
```

inside a service class.

Instead, the service should depend upon an abstraction:

```
public class MediaService {

    private final MediaRepository repository;

    public MediaService(MediaRepository repository) {
        this.repository = repository;
    }
}
```

Spring should provide the appropriate implementation.

You should demonstrate understanding of:

- Spring Beans
- ApplicationContext
- Inversion of Control
- Dependency Injection
- Constructor injection
- Configuration
- Interfaces and implementations

---

# 7\. Spring Configuration

Because this project deliberately excludes Spring Boot, you are expected to configure Spring yourself.

You may use Java-based configuration, XML configuration, or an appropriate combination.

For example:

```
@Configuration
@ComponentScan("com.example.medialibrary")
public class ApplicationConfig {
}
```

The application should create an appropriate Spring `ApplicationContext`.

Conceptually:

```
main()
   |
   v
ApplicationContext
   |
   +-- UserService
   +-- MediaService
   +-- RentalService
   +-- AdminService
   +-- UserRepository
   +-- MediaRepository
   +-- LoanRepository
   +-- ...
```

 The exact configuration approach is your choice.

---

# 8\. Database Abstraction

One of the most important requirements is that the database implementation must be replaceable.

The service layer must not be tightly coupled to SQLite.

For example:

```
public interface MediaRepository {

    Media findById(int id);

    List<Media> findAll();

    void save(Media media);
}
```

 You might then implement:

```
MediaRepository
       ^
       |
       +---- SQLiteMediaRepository
       |
       +---- OtherMediaRepository
```

The service layer should depend on:

```
MediaRepository
```

rather than:

```
SQLiteMediaRepository
```

### Required behaviour

If the company decided to replace SQLite with another database technology, you should be able to create a different repository implementation and change the Spring configuration without changing the core business logic.

For example:

```
                    +-----------------------+
                    |    MediaService       |
                    +-----------------------+
                              |
                              v
                    +-----------------------+
                    |   MediaRepository     |
                    |      interface        |
                    +-----------------------+
                       ^               ^
                       |               |
             +---------+       +-------+---------+
             |                           |
   SQLiteMediaRepository       OtherMediaRepository
```

You must include a short explanation in your README explaining how this has been achieved.

---

# 9\. Persistence

The application must use **SQLite** as its database.

You may implement persistence using:

- JDBC
- JPA
- A combination of JDBC and JPA

You are expected to demonstrate appropriate use of the chosen persistence technology.

The database should contain enough information to support all required functionality.

Possible tables might include:

```
users
roles
media
media_formats
loans
waiting_list
```

This is only a suggestion.

You are responsible for designing an appropriate database schema.

---

# 10\. Database Design

Your database design should demonstrate an understanding of relational database principles.

Consider:

- Primary keys
- Foreign keys
- Relationships
- Appropriate data types
- Constraints
- Referential integrity
- Avoiding unnecessary duplication

You should provide the SQL required to initialise the database.

For example:

```
database/
    schema.sql
    seed.sql
```

The application should either:

1. Be capable of creating the required database structure when first run, or
2. Provide clear instructions for creating and initialising the database.

---

# 11\. Users

The system must support users.

Each user should have at least:

- A unique ID
- A username
- A role

There are two roles:

```
ADMIN
USER
```

You may add other fields if useful, but these are the minimum requirements.

---

# 12\. User Permissions

## Standard users

A standard user should be able to:

- View media
- Search for media
- Rent media
- Return media
- Renew media
- View their current loans
- Join a waiting list

## Administrators

An administrator should have the standard functionality plus administrative functionality.

An administrator must be able to:

- Add books
- View appropriate media/inventory information
- Change books from `ON_ORDER` to `AVAILABLE`

You may add additional administrative functionality if desired.

The application must enforce the distinction between `ADMIN` and `USER`.

A normal user must not be able to perform an administrator-only operation simply by selecting the corresponding command from the command line.

---

# 13\. Media

The library contains five media types:

- Movie
- TV
- Music
- Podcast
- Book

Each media item should contain appropriate information.

At minimum, media should have:

- ID
- Title
- Media type
- Digital format
- Quantity/inventory information

You may add additional fields where appropriate.

Examples might include:

```
Movie
- Title
- Director
- Release year
- Format
```

or:

```
Music
- Title
- Artist
- Album
- Format
```

You do not need to implement all of these additional properties.

The important requirement is that the system supports the five required media types.

---

# 14\. Digital Media Formats

All media formats in this system represent **digital formats**.

Physical formats such as DVDs, CDs, vinyl records, hardcover books, etc. are **not required**.

The format must be stored with the media item.

Examples include:

### Movie

- MP4
- MKV
- MOV
- AVI

### TV

- MP4
- MKV
- MOV
- AVI

### Music

- MP3
- AAC
- FLAC
- WAV
- OGG

### Podcast

- MP3
- AAC
- M4A
- OGG

### Book

- EPUB
- PDF
- MOBI
- AZW
- TXT

You do not have to use these exact formats.

The important requirements are:

1. A media item has a digital format.
2. The format is stored in the database.
3. The format is displayed to users where appropriate.
4. The format is appropriate for the media type.
5. The design prevents or appropriately handles invalid media/format combinations.

For example:

```
Title: The Matrix
Type: Movie
Format: MP4
```

and:

```
Title: The Hobbit
Type: Book
Format: EPUB
```

An `EPUB` format would not be an appropriate format for a movie.

You may implement formats using:

- Java enums
- Database lookup tables
- A combination of enums and database tables
- Another appropriate design

You should be able to explain your decision.

---

# 15\. Media Quantity and Inventory

A media item may have multiple available copies/licences.

The system must track its inventory.

The required inventory states are:

- **AVAILABLE**
- **ON\_LOAN**
- **ON\_ORDER**

For example:

```
Title: The Matrix
Type: Movie
Format: MP4

Quantity: 5
Available: 3
On Loan: 2
On Order: 0
```

The inventory must remain consistent.

For example:

```
Available + On Loan + On Order = Quantity
```

The system must prevent a user from renting an item when there are no available copies.

---

# 16\. Renting Media

A standard user should be able to rent an available media item.

The rental period is:

**7 days**

When a rental is created, the system should record at least:

- User
- Media item
- Rental date
- Due date
- Return information/status

For example:

```
Rental date: 1 October
Due date:    8 October
```

When a media item is rented:

```
Available -> On Loan
```

For example:

```
Before:

Available: 3
On Loan:   2

After:

Available: 2
On Loan:   3
```

The system must not allow a user to rent media if there are no available copies.

---

# 17\. Multiple Copies

The system must correctly handle media with multiple copies.

For example:

```
The Hobbit
Quantity: 5
Available: 3
On Loan: 2
On Order: 0
```

If one user rents a copy:

```
Available: 2
On Loan: 3
On Order: 0
```

If one copy is returned:

```
Available: 3
On Loan: 2
On Order: 0
```

Do not model inventory purely as a single Boolean such as:

```
boolean available;
```

when the media item has multiple copies.

The system should correctly maintain quantities.

---

# 18\. Returning Media

A user must be able to return a media item before the seven-day rental period expires.

When media is returned:

```
ON_LOAN -> AVAILABLE
```

The corresponding loan should be marked as returned.

The system should record an appropriate return date/time.

The system must prevent a user from returning media they do not currently have on loan.

For example:

```
Before:

Available: 1
On Loan:   2

User returns one copy.

After:

Available: 2
On Loan:   1
```

---

# 19\. Renewing Loans

Users can renew a loan.

A renewal extends the rental period by another **7 days**.

For example:

```
Current due date:
8 October

Renewed due date:
15 October
```

However, a user **must not be allowed to renew an item if another user is waiting for that item**.

For example:

```
The Hobbit

User A:
Currently has the item on loan.

Waiting list:
1. Bob
2. Sarah
```

 If User A attempts to renew:

```
Renewal rejected.

Another user is waiting for this item.
```

 If nobody is waiting:

```
Renewal permitted.

Due date extended by 7 days.
```

 This rule should be implemented in the **service/business layer**, not directly in the command-line interface.

---

 # 20\. Waiting List

 The system must support a waiting list for media that currently has no available copies.

 For example:

```
The Hobbit

Available: 0
On Loan:   2

Waiting list:
1. Bob
2. Sarah
3. John
```

The waiting list should maintain an appropriate order.

A reasonable default is **first-come, first-served**.

The system should be able to determine:

- Whether somebody is waiting
- How many users are waiting
- Who is first
- Whether the current borrower is permitted to renew

You should decide and document what happens when a copy is returned while users are waiting.

---

# 21\. Books

Books have a special requirement.

When an administrator adds a new book, it must initially have the status:

```
ON_ORDER
```

For example:

```
Administrator adds:

Title: Clean Code
Type: Book
Format: EPUB
Quantity: 3

Status:
ON_ORDER
```

The book should not immediately become available for rental.

An administrator must subsequently be able to change the book's status to:

```
AVAILABLE
```

once the books/licences have arrived.

---

# 22\. Book Inventory

Books follow the same general inventory model as the other media.

For example:

```
Clean Code
Format: EPUB
Quantity: 3
Available: 0
On Loan: 0
On Order: 3
```

After the administrator receives the books:

```
Clean Code
Format: EPUB
Quantity: 3
Available: 3
On Loan: 0
On Order: 0
```

If one copy is rented:

```
Available: 2
On Loan: 1
On Order: 0
```

If the book is returned:

```
Available: 3
On Loan: 0
On Order: 0
```

Returned books must therefore increase the available count.

---

# 23\. Command-Line Interface (Optional)

The user interface should be a simple command-line application.

You do not need to create:

- A web application
- REST APIs
- A graphical user interface

 A possible menu is:

```
===========================
       MEDIA LIBRARY
===========================

1. Login
2. List media
3. Search media
4. Rent media
5. Return media
6. Renew rental
7. View my rentals
8. Join waiting list
9. Admin
0. Exit

Select:
```

You do not have to use this exact menu.

The command-line layer should primarily deal with:

- Reading input
- Displaying output
- Calling services
- Displaying user-friendly errors

The CLI should **not contain the core business rules**.

For example, the CLI should not decide whether:

```
another user is waiting
```

and therefore whether renewal is allowed.

That decision belongs in the service layer.

---

# 24\. Suggested Service Layer

You may structure your service layer however you wish.

A possible design is:

```
UserService
MediaService
RentalService
AdminService
```

Alternatively, related functionality could be combined into fewer services.

Possible service operations include:

```
rentMedia(userId, mediaId)

returnMedia(userId, mediaId)

renewRental(userId, mediaId)

addToWaitingList(userId, mediaId)

addBook(...)

makeBookAvailable(mediaId)
```

The service layer should contain the business rules.

For example:

```
rentMedia()
    |
    +-- Does user exist?
    |
    +-- Is user allowed to rent?
    |
    +-- Does media exist?
    |
    +-- Is a copy available?
    |
    +-- Create loan
    |
    +-- Update inventory
    |
    +-- Complete operation
```

---

# 25\. Repository/DAO Layer

The service layer should communicate with the database through interfaces.

For example:

```
public interface UserRepository {
    User findById(int id);
    User findByUsername(String username);
    List<User> findAll();
}
```

```
public interface MediaRepository {
    Media findById(int id);
    List<Media> findAll();
    void save(Media media);
    void update(Media media);
}
```

```
public interface LoanRepository {
    Loan findById(int id);
    List<Loan> findActiveLoansForUser(int userId);
    void save(Loan loan);
    void update(Loan loan);
}
```

These are examples only.

Your own design may differ.

The important requirement is that the service layer depends on **interfaces**.

---

# 26\. Error Handling

The application should handle invalid operations appropriately.

Examples include:

- User does not exist
- Media item does not exist
- User attempts to rent unavailable media
- User attempts to return media they do not have
- User attempts to renew media when another user is waiting
- Non-admin user attempts an administrator operation
- Invalid media format
- Invalid quantity
- Database failure
- Invalid command-line input

Use appropriate Java exception handling.

Avoid silently swallowing errors:

```
try {
    // ...
} catch (Exception e) {
    // ignore
}
```

Errors should be handled meaningfully.

You may create your own domain exceptions where appropriate, for example:

```
MediaNotFoundException
MediaUnavailableException
LoanNotFoundException
RenewalNotAllowedException
AccessDeniedException
```

These are suggestions, not mandatory class names.

---

# 27\. Transactions

For operations that change multiple pieces of data, consider whether they should be performed as a single transaction.

For example, renting media may involve:

```
1. Check availability
2. Create loan
3. Decrease available quantity
4. Increase on-loan quantity
```

These operations should not leave the database in a partially updated state.

You should consider appropriate transaction handling for:

- Renting
- Returning
- Renewing
- Updating inventory
- Other operations that modify related records

Transaction handling is particularly important if you choose to implement the optional concurrency extension.

---

# 28\. Initial Test Data

Provide enough initial data to demonstrate the application.

For example:

### Users

```
admin
alice
bob
charlie
```

with appropriate roles.

### Media

Include examples of all five types:

```
Movie
TV
Music
Podcast
Book
```

Use several different digital formats.

For example:

```
Movie: The Matrix
Format: MP4

TV: Planet Earth
Format: MKV

Music: Random Access Memories
Format: FLAC

Podcast: Technology Today
Format: MP3

Book: Clean Code
Format: EPUB
```

These are examples only; you may choose your own data.

Include enough inventory to demonstrate:

- Available media
- Media on loan
- Media with no available copies
- Books on order

---

# 29\. Required Demonstration

Your application should demonstrate the following scenarios.

## Scenario 1 — Normal Rental

1. Log in as a normal user.
2. Display available media.
3. Rent an available item.
4. Confirm that the inventory has changed.
5. Display the user's current rental.
6. Show the seven-day due date.

---

## Scenario 2 — Early Return

1. Rent an item.
2. Return it before the due date.
3. Confirm the loan is marked as returned.
4. Confirm the available quantity has increased.

---

## Scenario 3 — Renewal

1. Rent an item.
2. Renew the item.
3. Confirm the due date has moved by seven days.

---

## Scenario 4 — Waiting List

1. Ensure an item has no available copies.
2. Have another user join the waiting list.
3. Attempt to renew the item as the current borrower.
4. Demonstrate that the renewal is rejected because another user is waiting.

---

## Scenario 5 — Book Ordering

1. Log in as an administrator.
2. Add a new book.
3. Confirm that its initial status is `ON_ORDER`.
4. Change the book to `AVAILABLE`.
5. Confirm that the book can now be rented.
6. Rent the book.
7. Return the book.
8. Confirm that the available count increases.

---

## Scenario 6 — Access Control

Demonstrate that:

```
USER
```

cannot perform an administrator-only operation.

For example:

```
User attempts to add a book.

Operation rejected:
Administrator privileges required.
```

---

# 30\. Testing

You should include automated tests for important business rules.

At minimum, test several of the following:

- A user can rent available media.
- A user cannot rent unavailable media.
- A rental lasts seven days.
- A user can return a rental early.
- Returning a rental increases available inventory.
- A user can renew when nobody is waiting.
- A user cannot renew when somebody is waiting.
- A non-admin cannot perform an admin operation.
- A newly added book starts as `ON_ORDER`.
- An `ON_ORDER` book can be made available by an administrator.
- Invalid media/format combinations are rejected if your design enforces this.
- Inventory counts remain consistent.

Tests should particularly focus on the **service/business layer**.

You may use mocks, stubs, fakes, or other test doubles where appropriate.

---

# 31\. Code Quality

Your solution will be assessed not only on whether it works, but also on the quality of the implementation.

Consider:

- Meaningful class and method names
- Appropriate encapsulation
- Single responsibility
- Appropriate use of interfaces
- Low coupling
- Avoiding duplicated code
- Clear exception handling
- Appropriate Java collections
- Appropriate use of enums
- Readable SQL
- Appropriate transaction boundaries
- Sensible package structure
- Useful comments/documentation

Do not over-engineer the application.

A simple, well-structured solution is preferable to a large but unnecessarily complicated system.

---

# 32\. Optional Extension 1 — Overdue Rentals

**Estimated additional time: 15 minutes**

Add support for identifying overdue rentals.

The system should be able to display something such as:

```
OVERDUE RENTALS

User: Alice
Media: The Matrix
Due: 20 September
Days overdue: 5
```

Use Java's date/time API appropriately.

You should decide and document whether an overdue item:

- Can be renewed
- Can be returned normally
- Has any other restrictions

---

# 33\. Optional Extension 2 — Search and Filtering

**Estimated additional time: 15 minutes**

Improve the media search functionality.

Allow users to search/filter by one or more of:

- Title
- Media type
- Digital format
- Availability

For example:

```
Search: Tolkien

Results:

1. The Hobbit
   Type: Book
   Format: EPUB
   Available: 2

2. The Lord of the Rings
   Type: Book
   Format: PDF
   Available: 0
```

The search may be implemented in the service layer, database layer, or a combination, provided the architecture remains sensible.

---

# 34\. Optional Extension 3 — Waiting List Notifications

**Estimated additional time: 15 minutes**

Improve the waiting-list functionality.

When a media item is returned and another user is waiting, the system should indicate that the item is now available to the next user.

For example:

```
The Hobbit has been returned.

Bob is first on the waiting list.
```

You may implement this as a console notification.

You do not need to implement real email or SMS functionality.

---

# 35\. Optional Extension 4 — Transaction and Concurrency Protection

**Estimated additional time: 15 minutes**

Improve the persistence layer so that renting and returning media are handled safely as database transactions.

Consider what could happen if two users attempt to rent the final available copy at approximately the same time.

For example:

```
Available copies: 1

User A -> attempts to rent
User B -> attempts to rent
```

The system must not accidentally create two successful loans for one available copy.

Implement appropriate transaction/concurrency handling and document your approach.

---

# 36\. Suggested Project Structure

The following is an example only.

You may use a different structure if you can justify it.

```
src/
├── main/
│   ├── java/
│   │   └── com/company/medialibrary/
│   │       ├── Main.java
│   │       │
│   │       ├── config/
│   │       │   └── ApplicationConfig.java
│   │       │
│   │       ├── model/
│   │       │   ├── User.java
│   │       │   ├── Role.java
│   │       │   ├── Media.java
│   │       │   ├── MediaType.java
│   │       │   ├── MediaFormat.java
│   │       │   ├── Loan.java
│   │       │   └── ...
│   │       │
│   │       ├── repository/
│   │       │   ├── UserRepository.java
│   │       │   ├── MediaRepository.java
│   │       │   ├── LoanRepository.java
│   │       │   └── ...
│   │       │
│   │       ├── repository/sqlite/
│   │       │   ├── SQLiteUserRepository.java
│   │       │   ├── SQLiteMediaRepository.java
│   │       │   ├── SQLiteLoanRepository.java
│   │       │   └── ...
│   │       │
│   │       ├── service/
│   │       │   ├── UserService.java
│   │       │   ├── MediaService.java
│   │       │   ├── RentalService.java
│   │       │   └── AdminService.java
│   │       │
│   │       └── cli/
│   │           └── CommandLineInterface.java
│   │
│   └── resources/
│       ├── database/
│       │   ├── schema.sql
│       │   └── seed.sql
│       └── application.properties
│
└── test/
    └── java/
        └── com/company/medialibrary/
            └── ...
```

Again, this is a suggestion rather than a mandatory structure.

---

# 37\. Deliverables

Submit a project containing the following.

## Required

1. Complete Java source code.
2. Spring Framework configuration.
3. SQLite database setup/schema.
4. Database repository/DAO implementations.
5. Repository/DAO interfaces.
6. Service layer.
7. Command-line interface.
8. Appropriate automated tests.
9. README/documentation.

---

# 38\. README Requirements

Your README should explain:

### Running the application

- How to build the project.
- How to run the application.
- How to initialise the database.

### Test accounts

Provide example accounts, such as:

```
admin
alice
bob
charlie
```

Clearly identify which account is an administrator.

### Architecture

Explain:

- The application layers.
- Which classes are Spring Beans.
- Where dependency injection occurs.
- Which interfaces are used.
- How the repository layer is separated from the service layer.

### Database abstraction

Explain:

- How the SQLite implementation works.
- Which interfaces abstract database access.
- How another database implementation could be substituted.
- Which Spring configuration would need to change.

### Design decisions

Explain any significant decisions you made, such as:

- Media class design
- Digital format representation
- Inventory design
- Waiting-list behaviour
- Loan design
- Transaction handling
- Error handling

### Extensions

Identify which optional extensions you completed.

---

# 39\. Assessment Criteria

The assessment will focus on demonstrating understanding rather than simply producing a working application.

| Area | What will be assessed |
| --- | --- |
| Java | OO design, collections, exceptions, enums, interfaces and general Java knowledge |
| Spring IoC | Correct use of Spring ApplicationContext and Beans |
| Dependency Injection | Dependencies injected rather than manually constructed |
| Abstraction | Service layer depends on interfaces rather than database implementations |
| Persistence | Appropriate JDBC/JPA implementation using SQLite |
| Database | Appropriate relational design and SQL |
| Business Logic | Correct rental, return, renewal and waiting-list rules |
| Inventory | Correct Available/On Loan/On Order handling |
| User Roles | Appropriate distinction between users and administrators |
| Digital Formats | Appropriate modelling and persistence of media formats |
| CLI | Clear and usable command-line interface |
| Testing | Tests covering important business rules |
| Code Quality | Readability, maintainability and sensible architecture |
| Documentation | Clear explanation of design and implementation decisions |

---

# 40\. Key Requirement Checklist

Before submitting, verify that your application can answer **yes** to all of the following:

## Java and Spring

- [ ] Is this a Java application?
- [ ] Does it use the Spring Framework?
- [ ] Does it **not** use Spring Boot?
- [ ] Are application components managed as Spring Beans?
- [ ] Is dependency injection used?
- [ ] Is an ApplicationContext used?
- [ ] Is there a service/business layer?
- [ ] Does the service layer depend on repository interfaces?
- [ ] Can the persistence implementation be replaced through DI/configuration?

## Database

- [ ] Is SQLite used for persistence?
- [ ] Is there an appropriate relational schema?
- [ ] Are primary and foreign keys used appropriately?
- [ ] Is database access separated from business logic?
- [ ] Is SQL/JDBC and/or JPA used appropriately?

## Users and Roles

- [ ] Are users supported?
- [ ] Are `ADMIN` and `USER` roles supported?
- [ ] Are administrator-only operations protected?

## Media

- [ ] Are movies supported?
- [ ] Are TV programmes/series supported?
- [ ] Is music supported?
- [ ] Are podcasts supported?
- [ ] Are books supported?
- [ ] Does every media item have a digital format?
- [ ] Are formats persisted?
- [ ] Are inappropriate media/format combinations handled appropriately?

## Inventory

- [ ] Can media have multiple copies/licences?
- [ ] Are available quantities tracked?
- [ ] Are on-loan quantities tracked?
- [ ] Are on-order quantities tracked?
- [ ] Do inventory counts remain consistent?
- [ ] Can unavailable media not be rented?

## Rentals

- [ ] Can users rent media?
- [ ] Are rentals for seven days?
- [ ] Can users return media early?
- [ ] Does returning media increase the available count?
- [ ] Can users renew rentals?
- [ ] Does renewal extend the rental by seven days?
- [ ] Is renewal prevented when another user is waiting?

## Waiting List

- [ ] Can users join a waiting list?
- [ ] Is waiting order maintained?
- [ ] Can the system determine whether another user is waiting?

## Books

- [ ] Can administrators add books?
- [ ] Do newly added books start as `ON_ORDER`?
- [ ] Can administrators change books to `AVAILABLE`?
- [ ] Can available books be rented?
- [ ] Does returning a book increase the available count?

## Command Line

- [ ] Can the application be operated through the command line?
- [ ] Is business logic kept out of the CLI?
- [ ] Are invalid commands/input handled appropriately?

## Testing

- [ ] Are important business rules tested?
- [ ] Are rental operations tested?
- [ ] Are return operations tested?
- [ ] Are renewal rules tested?
- [ ] Is the waiting-list rule tested?
- [ ] Are administrator permissions tested?
- [ ] Is book ordering tested?
- [ ] Is inventory behaviour tested?

---

# 41\. Final Objective

The goal of this exercise is **not** to build a production-scale media library.

The goal is to demonstrate that you understand how to build a small Java application using the **Spring Framework without Spring Boot**, and that you understand why software should be designed around abstractions and dependencies rather than tightly coupling business logic to a particular database technology.

Your architecture should resemble the following:

```
                  Spring IoC
                      |
                      v
             +------------------+
             |  Command Line UI |
             +------------------+
                      |
                      v
             +------------------+
             |  Service Layer   |
             |  Business Logic  |
             +------------------+
                      |
                      | depends on
                      v
             +------------------+
             | Repository       |
             | Interface        |
             +------------------+
                    ^       ^
                    |       |
                    |       |
       +------------+       +----------------+
       |                                     |
+----------------------+          +----------------------+
| SQLite Repository    |          | Other Repository    |
| Implementation       |          | Implementation      |
+----------------------+          +----------------------+
       |
       v
+----------------------+
|      SQLite DB       |
+----------------------+
```

The key question you should be able to answer at the end of the exercise is:

> **If the company decided tomorrow to replace SQLite with another database, how much of the application would need to change?**

Your architecture should make the answer:

> **The database implementation and its Spring configuration, rather than the service/business logic.**

This exercise is intended to demonstrate that you understand not only **how to make the application work**, but also **how to structure software so that it can be changed and maintained.**