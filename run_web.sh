#!/bin/sh

cd myproject
echo "Sleeping 10 sec. Waiting for db to come up"
sleep 10
su -m myuser -c "python manage.py migrate"
su -m myuser -c "python manage.py runserver 0.0.0.0:8000"
