from datetime import datetime

from celery import shared_task


@shared_task(bind=True)
def demo_celery_function(self):
    for i in range(100):
        for j in range(i):
            i*j
    print("test")

@shared_task
def crontab_ping_test():
    print("printing every 2 min interval")