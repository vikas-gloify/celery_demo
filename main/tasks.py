import logging
from datetime import datetime

from celery import shared_task
from django.contrib.auth.models import User

from demo_celery.celery import celery_app


@shared_task(bind=True)
def demo_celery_function(self):
    for i in range(1000):
        for j in range(i):
            i*j
    print("test")

@celery_app.task(queue='myqueue',bind=True)
def crontab_ping_test(self):
    running_on_interval()

def running_on_interval():
    for i in range(100):
        for j in range(i):
            i*j
        logging.info(f"schedued {i}")