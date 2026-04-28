# Auth server demo

To run this demo

```
npx ts-node-dev src/index.ts
```

Login using POST request to

```
http://localhost:3000/login
```

You will need to pass the following as the body;

```
{
  "username": "alice",
  "password": "password123"
}
```

You will receive the response of;

```
{
    "token": "ewofhfwufwuvikvbu4895439853urehg..."
}

## Access the data

Use

```
http://localhost:3000/users
```

You will need to pass the following in the header;

```
Authorization: Bearer <your_token_here>
```

Example response;

```
[
  { "username": "alice", "password": "password123" },
  { "username": "bob", "password": "secret456" },
  { "username": "charlie", "password": "qwerty789" }
]
```