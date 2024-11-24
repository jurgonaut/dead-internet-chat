Welcome to Dead Internet Chat!

This is a WIP chat app made with Flask, Redis and Open AI. The idea is to have a chat where humans don't know if they are interacting with other humans or with an AI. I uses Redis for pushing messages to the client with Event Source and as a DB. I know Redis is not supposed to be used for persistent storage, but I wanted to explore Redis.

All the services run in Docker and in addition you can enable Flask debugging inside the container. First you need to create the `env` files with
```bash
cp env/flask.example.env env/flask.env
cp env/redis.example.env env/redis.env
```

Start the local environment with:
```bash
MY_UID="$(id -u)" MY_GID="$(id -g)" docker-compose --profile dev --profile web up --build
```
We set the `MY_UID` and `MY_GID` so that the user inside the docker container matches the user on the host, this is so that we prevent permissions issues.

Then you use the running container for developing and debugging ([more info](https://code.visualstudio.com/docs/devcontainers/containers)). You can use the `launch.json.example` for setting up the debugging configuration.

You can create a basic conversation by navigating to the url `localhost:5000/generate_chat`. And you can trigger an Chat GPT response by hitting the url `localhost:5000/bot-response`. Not that you must add your API key to the `env` file.

You can run basic performance stress test with:
```bash
docker-compose --profile perf up
```

TODO
- currently the users added are never removed, when we add an user we also set a timestamp. We could use that to automatically remove an user after some time
- there are no tests for the Event Source, it would be nice to find a way to test that
- The bot has a very limited personality, we could add multiple traits to make it more interesting
