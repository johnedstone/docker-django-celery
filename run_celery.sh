#!/bin/sh

cd picha
# su -m myuser -c "celery worker -A picha -Q default -n default@%h"
su -m myuser -c "celery worker -A picha -Q default -n default@%h -l info"
