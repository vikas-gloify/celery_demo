import os

from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE","demo_celery.settings")


celery_app = Celery("demo_celery")
celery_app.config_from_object(settings, namespace="CELERY")

# CELERY_BEAT_SCHEDULER='django_celery_beat.schedulers:DatabaseScheduler'

celery_app.conf.update(
    {
        "broker_url": "amqp://root:root@rabbitmqserver",
        "task_serializer": "json",
        "task_acks_late": True,
        "result_serializer": "json",
        "result_backend": "rpc://",
        "accept_content": ["json"],
        "worker_prefetch_multiplier": 1,
        "result_extended": True,
        "task_reject_on_worker_lost": True,
        "broker_connection_retry_on_startup":True
    }
)

celery_app.conf.task_routes = {
    "main.tasks.demo_celery_function":{"queue":"testq"},
    "main.tasks.crontab_ping_test":{"queue":"myqueue"}
}




celery_app.conf.beat_schedule = {
    "task-ping-every-2-min": {
        "task": "main.tasks.crontab_ping_test",
        "schedule": 60,
        "args": (),
    },
}

celery_app.autodiscover_tasks()