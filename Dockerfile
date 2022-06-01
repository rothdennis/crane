FROM python:3.10-alpine
LABEL org.opencontainers.image.source https://github.com/rothdennis/crane
WORKDIR /crane
# RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
CMD python3 app/main.py