### Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r reqirements.txt
```

### Commands
Not that the containers must be running

Flush all the data in `Redis`
```bash
docker-compose exec redis redis-cli --user default --pass pass flushall
```

Run tests in docker.
```bash
docker-compose exec redis redis-cli --user default --pass pass flushall && docker-compose run flask pytest -s src
```
