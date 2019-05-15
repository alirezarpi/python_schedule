
# from __future__ import absolute_import
from celery import Celery

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'python_schedule.settings')

from django.conf import settings


app = Celery('python_schedule',
            backend='amqp',
            broker='amqp://localhost//')
            
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))

