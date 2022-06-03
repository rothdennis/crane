# Crane 🏗

Web UI for Docker

## Installation

### via CLI

```
docker run -d -p 9000:8000 \
-v /var/run/docker.sock:/var/run/docker.sock \
ghcr.io/rothdennis/crane:latest
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

## Screenshots

### Index
![Index](https://raw.githubusercontent.com/rothdennis/crane/main/images/index.png "Index")

### Containers Overview
![Containers](https://raw.githubusercontent.com/rothdennis/crane/main/images/containers.png "Containers")

### Container Detail
![Container Detail](https://raw.githubusercontent.com/rothdennis/crane/main/images/container_view.png "Container Detail")

### Volumes Overview
![Volumes](https://raw.githubusercontent.com/rothdennis/crane/main/images/volumes.png "Volumes")

### Networks Overview
![Networks](https://raw.githubusercontent.com/rothdennis/crane/main/images/networks.png "Networks")

### Images Overview
![Images](https://raw.githubusercontent.com/rothdennis/crane/main/images/images.png "Images")
