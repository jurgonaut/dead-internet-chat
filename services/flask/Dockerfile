FROM docker.io/python:3.13-slim-bookworm

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y gcc libpq-dev postgresql libevent-dev python3-dev

RUN mkdir -p /app/src
WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY entrypoint.sh .
COPY src/ ./src

CMD ["./entrypoint.sh"]

