#!/bin/bash

# Running Database migrations
python manage.py migrate --noinput

# Running Application with uWSGI
exec gunicorn url_shortner.wsgi:application \
    --bind=0.0.0.0:8000 \
    --log-level=debug \
    --access-logfile=$PWD/accesslog.log \
    --workers=4 \
    --error-logfile=$PWD/errorlog.log \
"$@"