#!/bin/sh

python /test_alive.py

cp -r /app/media/* /app/media_prod

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py collectstatic --no-input

DJANGO_SUPERUSER_PASSWORD=$SUPER_USER_PASSWORD python manage.py createsuperuser --username $SUPER_USER_NAME --email $SUPER_USER_EMAIL --noinput

gunicorn django_app.wsgi:application --bind 0.0.0.0:8000