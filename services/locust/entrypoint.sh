#!/bin/bash
set -eo pipefail

if [ ! -z "${USERS}" ] && [ ! -z "${TARGET_HOST}" ] && [ ! -z "${USERNUM}" ] && [ ! -z "${SPAWNRATE}" ] && [ ! -z "${TIME}" ]; then
    echo "Running locust in headless mode"
    locust --headless --users "${USERNUM}" --spawn-rate "${SPAWNRATE}" -t "${TIME}" -H "${TARGET_HOST}" -f src/locustfile.py "${USERS}"
else
    echo "Running locust with web interface"
    locust -f src/locustfile.py
fi
