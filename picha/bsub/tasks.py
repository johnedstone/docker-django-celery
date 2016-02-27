from functools import wraps
from time import sleep

from picha.celery import app
from .models import Job


def update_job(fn):
    @wraps(fn)
    def wrapper(job_id, *args, **kwargs):
        job = Job.objects.get(id=job_id)
        job.status = 'started'
        job.save()
        try:
            result = fn(*args, **kwargs)
            job.result = result
            job.status = 'finished'
            job.save()
        except:
            job.result = None
            job.status = 'failed'
            job.save()
    return wrapper


@app.task
@update_job
def bootstrap(**kwargs):
    """Bootstrap chef client"""
    print('{}'.format(kwargs))
    sleep(50)
    return 'Bootstrap done' 

TASK_MAPPING = {
    'bootstrap': bootstrap,
}
