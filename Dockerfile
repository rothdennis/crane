FROM python:3.10-slim-buster
LABEL org.opencontainers.image.source https://github.com/rothdennis/crane
WORKDIR /crane
# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["docker-entrypoint.sh"]