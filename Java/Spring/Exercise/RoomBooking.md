## Mini Project: Co-Working Space Booking System

The scenario is a modern business application, but deliberately small enough to complete in around **3 hours**.

## The Scenario

A company operates a network of co-working spaces. Employees can book different types of workspaces for a day.

There are:

- Employees
- Bookings
- Workspaces
- Different types of workspaces
- A `BookingManager` that coordinates everything

The system needs to:

- Validate bookings
- Calculate costs
- Handle errors
- Produce a simple summary

This gives you very natural opportunities to test:

- Classes
- Constructors
- Inheritance
- Polymorphism
- Exceptions
- Unit testing
- Object interaction

---

# The Brief

You have been asked to develop the core business logic for a small co-working space booking system.

The system allows employees to book workspaces for a specified number of hours.

Different workspace types have different pricing rules.

The application must prevent invalid bookings and calculate the cost of each booking.

There is **no requirement for a database, GUI or web application**. Concentrate on clean, maintainable Java code and unit tests.

---

## 1\. Employee

Create an `Employee` class.

An employee has:

- `employeeId`
- `name`
- `department`

An employee should be created using a constructor.

### Example

```
Employee employee =
    new Employee("E1001", "Sarah Jones", "Marketing");
```

### Business Rules

- Employee ID cannot be blank.
- Name cannot be blank.
- An employee cannot make a booking for zero or negative hours.

---

## 2\. Workspace

Create an abstract `Workspace` class.

Every workspace has:

- `workspaceId`
- `description`
- `capacity`

It should also define a method for calculating the booking cost.

For example:

```
public abstract BigDecimal calculateCost(int hours);
```

This is where I'd expect them to demonstrate **inheritance and polymorphism**.

---

## 3\. Different Workspace Types

Implement three workspace types.

### Desk

A standard desk costs:

**£10 per hour**

### MeetingRoom

A meeting room costs:

**£30 per hour**

But it has a **minimum booking of 2 hours**.

### PrivateOffice

A private office costs:

**£50 per hour**

Bookings of **4+ hours** receive a **15% discount**.

Therefore:

| Workspace | Pricing |
| --- | --- |
| Desk | `10 × hours` |
| MeetingRoom | `30 × hours` |
| PrivateOffice | `50 × hours`, with discount where applicable |

The important part is that the booking system should be able to do:

```
Workspace workspace = ...;

BigDecimal cost = workspace.calculateCost(hours);
```

without knowing whether it has a `Desk`, `MeetingRoom` or `PrivateOffice`.

That's your **polymorphism test**.

---

## 4\. Booking

Create a `Booking` class.

A booking contains:

- `bookingId`
- `Employee`
- `Workspace`
- `numberOfHours`

### Example

```
Booking booking = new Booking(
    "B001",
    employee,
    workspace,
    4
);
```

The booking should be responsible for calculating its total cost.

For example:

```
booking.getTotalCost();
```

This gives you a nice chain of object interaction:

```
Booking
   ↓
Employee
   ↓
Workspace
   ↓
calculateCost()
```

---

## 5\. Booking Manager

Create:

```
BookingManager
```

This is responsible for managing employees, workspaces and bookings.

### Potential Methods

```
registerEmployee(Employee employee)

registerWorkspace(Workspace workspace)

createBooking(
    String bookingId,
    String employeeId,
    String workspaceId,
    int hours
)

cancelBooking(String bookingId)

getBooking(String bookingId)

getTotalRevenue()
```

You don't need to prescribe every method.

I'd actually tell them:

> **Design the public API of `BookingManager` yourself, but the application must support the following business operations.**

That makes it much more interesting as an assessment.

---

## 6\. Business Rules & Exceptions

This is where the exercise becomes useful.

The system should handle situations such as:

- Employee does not exist
- Workspace does not exist
- Booking already exists
- Booking duration is invalid
- Workspace is already booked
- Meeting room booking is too short

Ask them to create appropriate custom exceptions.

For example:

```
EmployeeNotFoundException
WorkspaceNotFoundException
BookingAlreadyExistsException
WorkspaceUnavailableException
InvalidBookingException
```

Don't require those exact names.

You're looking at whether they understand **when an exception is appropriate**, rather than whether they can copy a class declaration.

---

## 7\. Unit Tests

I'd make testing explicitly part of the deliverable.

### Minimum: 10 Meaningful JUnit Tests

For example:

1. Employee can be created.
2. Blank employee name is rejected.
3. Desk calculates correct cost.
4. Meeting room calculates correct cost.
5. Meeting room rejects booking under 2 hours.
6. Private office applies discount.
7. Booking calculates correct total.
8. Duplicate booking is rejected.
9. Unknown employee is rejected.
10. Unknown workspace is rejected.

Then add:

> **At least two tests must test exceptional behaviour.**

This stops them from writing ten variations of:

```
assertEquals(100, result);
```

---

# Additional Requirement

The business has decided to introduce a new workspace type called `TrainingRoom`.

### TrainingRoom Rules

- Training rooms cost **£75 per hour**.
- Bookings of **6 or more hours** receive a **20% discount**.

Add this functionality.

You should **not need to modify `BookingManager`** to support the new workspace type.

If you have implemented the system using polymorphism properly, you should essentially be able to write:

```
public class TrainingRoom extends Workspace {
    ...
}
```

 and have the existing booking system work.

 If you have written a giant:

```
if (workspace instanceof Desk) {
    ...
} else if (workspace instanceof MeetingRoom) {
    ...
} else if (workspace instanceof PrivateOffice) {
    ...
}
```

 it will immediately expose your design.

---

# Suggested 3-Hour Timeline

| Time | Activity |
| --- | --- |
| 0:00–0:15 | Read requirements / design |
| 0:15–1:15 | Core classes and object model |
| 1:15–1:45 | Exceptions and validation |
| 1:45–2:25 | JUnit tests |
| 2:25–2:50 | `TrainingRoom` change |
| 2:50–3:00 | Clean-up / prepare walkthrough |

If you feel like you need more of a challenge, create a **console menu**, rather than just using `Scanner`.

---

# Why I Like This One

It gives you a surprisingly good spread of Java skills:

```
                 BookingManager
                 /     |      \
                /      |       \
        Employee    Booking    Workspace
                              /    |     \
                             /     |      \
                          Desk  Meeting   Office
```

It provides opportunities to demonstrate:

- Object-oriented design
- Encapsulation
- Constructors
- Inheritance
- Abstract classes
- Polymorphism
- Exception handling
- Validation
- Collections
- `BigDecimal`
- JUnit testing
- Object collaboration
- Extensibility and maintainability