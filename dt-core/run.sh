#!/bin/sh

#export APP_MODULE=${APP_MODULE-app.main:app}
export APP_MODULE=app.main:app
export HOST=${HOST:-0.0.0.0}
export PORT=${PORT:-8001}

#echo $APP_MODULE
LOG_LEVEL="debug"
RELOAD=
if [ "${ENV}" = "dev" ]; then
    RELOAD=--reload
    LOG_LEVEL='debug'
fi 

echo "Starting up service..."
exec gunicorn -w $NUM_WORKERS -k uvicorn.workers.UvicornWorker --timeout $UNICORN_WORKER_TIMEOUT ${RELOAD} -b $HOST:$PORT "$APP_MODULE" --log-level $LOG_LEVEL