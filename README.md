# Crane 🏗

Web UI for Docker

## Build container images

docker build -t crane:0.1 -t crane:latest .

docker run -d -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock crane:0.1