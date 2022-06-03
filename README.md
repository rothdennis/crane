# Crane 🏗

Web UI for Docker

## Installation

### via CLI

```
docker run -d -p 9000:8000 -v /var/run/docker.sock:/var/run/docker.sock ghcr.io/rothdennis/crane:latest
```

### via `docker-compose`

```
services:
  crane:
    image: ghcr.io/rothdennis/crane:latest
    ports:
      - "8000:8000"
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```