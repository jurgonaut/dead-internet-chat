#!/bin/bash
set -euo pipefail

DEPLOY_ENV=${DEPLOY_ENV:-}
LOG_LEVEL=${LOG_LEVEL:-"INFO"}
RELOAD=""

cli_command=()

if [ $DEPLOY_ENV = "debug" ]; then
    export GEVENT_SUPPORT=True
    RELOAD="true"
    cli_command+=(debugpy --wait-for-client --listen 0.0.0.0:5678 -m)
fi

cli_command+=(gunicorn --bind 0.0.0.0:5000 --log-level="${LOG_LEVEL}" --chdir src wsgi:app -k gevent)

if [ $RELOAD = "true" ]; then
    cli_command+=(--reload)
fi

echo "${cli_command[@]}"

"${cli_command[@]}"
