Welcome to Dead Internet Chat!

This is a WIP chat app made with Flask, Redis and Open AI. The idea is to have a chat where humans don't know if they are interacting with other humans or with an AI. I uses Redis for pushing messages to the client with Event Source and as a DB. I know Redis is not supposed to be used for persistent storage, but is my tpy project and I don't care, I didn't feel like setting up a proper DB and wanted to explore Redis.

Run the local environment with:
```bash
docker-compose --profile dev --profile web  up --build
```
