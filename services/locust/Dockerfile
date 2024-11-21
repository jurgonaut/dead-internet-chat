# The latest supported python version is 3.6
FROM docker.io/python:3.6.15-slim-buster

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1

RUN mkdir -p /locust/src
WORKDIR /locust

COPY requirements.txt entrypoint.sh ./
RUN pip3 install -r requirements.txt
COPY src/ ./src

ENTRYPOINT ["./entrypoint.sh"]
