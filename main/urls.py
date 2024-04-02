from django.urls import path

from .views import celery_test

urlpatterns = [
    path('task',celery_test, name='first_task'),
]
