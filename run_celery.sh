#!/bin/sh

cd picha
su -m myuser -c "celery worker -A picha.celery -B -Q default -n default@%h -l info"
