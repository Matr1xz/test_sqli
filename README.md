# SQLi CTF Lab (Training Only)

⚠️ This project is intentionally vulnerable and must be used only in isolated CTF/lab environments.

## Run

```bash
docker compose up --build -d
```

Open: http://localhost:5000

## Credentials

- username: `alice`
- password: `alice`

## Features

- `/login` for authentication
- `/search` intentionally vulnerable to SQL injection
- Shows raw SQL query on search page for learning/debugging

## Stop

```bash
docker compose down
```