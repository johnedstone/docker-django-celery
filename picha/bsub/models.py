from django.db import models

class Job(models.Model):
    TYPES = (
      ('bootstrap', 'bootstrap'),
    )

    STATUSES = (
        ('pending', 'pending'),
        ('started', 'started'),
        ('finished', 'finished'),
        ('failed', 'failed'),
    )

    type = models.CharField(choices=TYPES, max_length=20)
    status = models.CharField(choices=STATUSES, max_length=20, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    fqdn = models.CharField(max_length=100)
    client_rb_path = models.CharField(max_length=100, blank=True)
    key_path = models.CharField(max_length=100, blank=True)
    result = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        super(Job, self).save(*args, **kwargs)
        if self.status == 'pending':
            from .tasks import TASK_MAPPING
            task = TASK_MAPPING[self.type]
            task.delay(job_id=self.id,
            fqdn=self.fqdn,
            client_rb=self.client_rb_path,
            key=self.key_path,
            )
