# simple_cd_jpa_spring_boot

A minimal Spring Boot JPA example using an in-memory H2 database.

## Run

1. Build the project:
   ```bash
   mvn clean package
   ```
2. Run:
   ```bash
   mvn spring-boot:run
   ```

## API

- `GET /api/cds` - list all CDs
- `GET /api/cds/{id}` - get CD by id
- `POST /api/cds` - create a CD

## Example JSON

```json
{
  "title": "Greatest Hits",
  "artist": "Example Band",
  "price": 12.50
}
```

## Seeded Sample Data

The application loads sample CDs automatically on startup:

- `Greatest Hits` by `Example Band`
- `Acoustic Sessions` by `Studio Artist`
