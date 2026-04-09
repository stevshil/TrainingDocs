# multi_db_cd_library

A Spring Boot JPA CD library with support for either H2 or MySQL.

## Run

Default profile: H2

```bash
cd Java/spring_boot/multi_db_cd_library
mvn spring-boot:run
```

MySQL profile:

```bash
mvn spring-boot:run -Dspring-boot.run.profiles=mysql
```

Or with environment variable:

```bash
SPRING_PROFILES_ACTIVE=mysql mvn spring-boot:run
```

## API

- `GET /api/cds` - list all CDs
- `GET /api/cds/{id}` - get a CD by id
- `POST /api/cds` - add a CD

## Seeded data

The application loads sample CDs on startup for both profiles.
