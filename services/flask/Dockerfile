FROM docker.io/python:3.13-slim-bookworm

ARG UID="1000"
ARG GID="1000"

# Disable pycache
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && \
    apt-get install -y gcc libpq-dev libevent-dev

RUN mkdir -p /app/src

COPY requirements.txt /app
RUN pip3 install -r /app/requirements.txt
COPY entrypoint.sh /app
COPY src/ /app/src

RUN groupadd -g $GID app-user && \
    useradd -ms /bin/bash -d /app -u $UID -g $GID app-user && \
    chown -R app-user:app-user /app

WORKDIR /app
USER app-user

CMD ["./entrypoint.sh"]
