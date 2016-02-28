## django with celery using docker-compose

The master branch is currently using docker-compose, base on the ideas from http://www.syncano.com/configuring-running-django-celery-docker-containers-pt-1/

References:
  - As noted above: http://www.syncano.com/configuring-running-django-celery-docker-containers-pt-1/
  - From: https://realpython.com/blog/python/asynchronous-tasks-with-django-and-celery/
  - See also http://michal.karzynski.pl/blog/2014/05/18/setting-up-an-asynchronous-task-queue-for-django-using-celery-redis/

### To Do
Figure out how to django createsuperuser programatically, but currently not needed.

#### The heart of the matter: docker-compose.yml

```javascript
db:
  image: postgres:9.4
  environment:
    - POSTGRES_PASSWORD=mysecretpassword
redis:
  image: redis:2.8.19
rabbitmq:
  image: tutum/rabbitmq
  environment:
    - RABBITMQ_PASS=mypass
  ports:
    - "5672:5672"
    - "15672:15672"
web:
  build: .
  command: ./run_web.sh
  volumes:
    - .:/app:z
  ports:
    - "9000:8000"
  links:
    - db:db
    - redis:redis
    - rabbitmq:rabbit
# This makes more sense than supervisord, for the moment
worker:
  build: .
  command: ./run_celery.sh
  volumes:
    - .:/app:z
  links:
    - db:db
    - rabbitmq:rabbit
    - redis:redis
```
