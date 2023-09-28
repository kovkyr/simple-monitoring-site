#!/bin/sh

if [ "$1" = cron ]; then
  python /app/manage.py crontab add
fi

exec "$@"
