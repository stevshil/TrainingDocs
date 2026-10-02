# Spring Boot RESTful Service

In this project we want you to refactor your Spring application into a Spring Boot REST API.

You can use either;
- [LendingLibrary](./LendingLibrary.md)
- [RoomBooking](./RoomBooking.md)

## Project structure

Ensure that you use a suitable package structure for your project to break down the responsibilities such as;
- Controller
    - For the REST API endpoints
- Services
    - Handling the business logic/process
- Data Access Object/ Repository
    - Getting the data from the database
- Entity
    - The table mappings
    - Table relationships

### Controller Example

```
@RestController
@RequestMapping("/api/bookings")
public class BookingController {

    private final BookingService bookingService;

    public BookingController(BookingService bookingService) {
        this.bookingService = bookingService;
    }

    @PostMapping
    public ResponseEntity<BookingResponse> createBooking(
            @RequestBody CreateBookingRequest request) {

        BookingResponse response =
                bookingService.createBooking(request);

        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(response);
    }

    @GetMapping("/{id}")
    public ResponseEntity<BookingResponse> getBooking(
            @PathVariable Long id) {

        BookingResponse response =
                bookingService.getBooking(id);

        return ResponseEntity.ok(response);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> cancelBooking(
            @PathVariable Long id) {

        bookingService.cancelBooking(id);

        return ResponseEntity.noContent().build();
    }
}
```

### Service Example

```
@Service
public class BookingService {

    public Booking createBooking(CreateBookingRequest request) {

        Employee employee =
            employeeRepository.findById(request.employeeId())
                .orElseThrow(EmployeeNotFoundException::new);

        Workspace workspace =
            workspaceRepository.findById(request.workspaceId())
                .orElseThrow(WorkspaceNotFoundException::new);

        if (request.hours() <= 0) {
            throw new InvalidBookingException("Hours must be positive");
        }

        if (bookingRepository.existsByWorkspaceAndDate(
                workspace, request.date())) {
            throw new WorkspaceUnavailableException();
        }

        Booking booking = new Booking(
            employee,
            workspace,
            request.hours()
        );

        return bookingRepository.save(booking);
    }
}
```

### DAO/Repository Example

```
@Repository
public interface BookingRepository
        extends JpaRepository<Booking, Long> {

    boolean existsByWorkspaceAndDate(
        Workspace workspace,
        LocalDate date
    );
}
```

### Entity Example

```
package com.tps.cd.Entity;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

@Entity
@Table(name = "compact_disc")
@Getter
public class CompactDiscLombok {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Setter
    private String title;

    @Setter
    private String artist;

    @Setter
    private Double price;

    public CompactDiscLombok() {}

    public CompactDiscLombok(String title, String artist, Double price) {
        this.title = title;
        this.artist = artist;
        this.price = price;
    }
}
```

## Error handling

Ensure that you provide suitable error handling in your application and make appropriate use of HTTP Response codes, not just JSON messages.

## Completion

At the end of the task you should be able to use [Postman](https://www.postman.com/) to check that your API is working.

## Add security

Once you have the above working consider adding a security token to the project.

All API requests should require a token being passed in the header, which the application can check to validate that you are logged in and have the correct role for the request being made.

The token is a 2 part process;

1. Login
    - The user must acquire a token from the login service
    - They must pass a valid username and password to receive the token
2. Passing the token
    - The token must be passed in the header for all requests
    - The service should ensure that the users token is valid
    - The service should check that the users role allows access to the requested endpoint/operation

## Completion

You should be able to test your entire service through Postman passing the token using the Bearer Token Authorization header.