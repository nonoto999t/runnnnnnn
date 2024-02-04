# Dockerfile
FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get clean

COPY script.py /

CMD ["python3", "/script.py"]
