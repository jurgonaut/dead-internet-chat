Welcome to Dead Internet Chat!

This is a WIP chat app made with Flask, Redis and Open AI. The idea is to have a chat where humans don't know if they are interacting with other humans or with an AI. I uses Redis for pushing messages to the client with Event Source and as a DB. I know Redis is not supposed to be used for persistent storage, but is my tpy project and I don't care, I didn't feel like setting up a proper DB and wanted to explore Redis.

All the services run in Docker and in addition you can enable Flask debugging inside the container. First you need to create the `env` files with
```bash
cp env/flask.example.env env/flask.env
cp env/redis.example.env env/redis.env
```
Then you need to enable the `launch.json` with
```bash
cp .vscode/launch.json.example .vscode/launch.json
```
After that you modify `localRoot` to point to the `src` folder in the `flask` service. Lastly you need to set the `env` variable `DEPLOY_ENV` to `debug`.

Run the local environment with:
```bash
docker-compose --profile dev --profile web up --build
```

You can create a basic conversation by navigating to the url `localhost:5000/generate_chat`. And you can trigger an Chat GPT response by hitting the url `localhost:5000/bot-response`. Not that you must add your API key to the `env` file.

You can run basic performance stress test with:
```bash
docker-compose --profile perf up
```

TODO
- currently the users added are never removed, when we add an user we also set a timestamp. We could use that to automatically remove an user after some time
- there are no tests for the Event Source, it would be nice to find a way to test that
- The bot has a very limited personality, we could add multiple traits to make it more interesting
