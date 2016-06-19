#!/bin/sh

cd myproject
sleep 10
su -m myuser -c "celery worker -A myproject.celeryconf -Q default -n default@%h"
