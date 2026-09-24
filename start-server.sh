#!/usr/bin/env bash
# start-server.sh
echo "Hello from Project Eurotort - Database on European Tort Law"

uv run manage.py collectstatic --no-input
uv run manage.py migrate --no-input
uv run gunicorn djangobaseproject.wsgi --user www-data --bind 0.0.0.0:8010 --workers 3 & nginx -g "daemon off;"
