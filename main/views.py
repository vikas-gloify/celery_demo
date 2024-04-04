from django.http import HttpResponse
from django.shortcuts import render

from main.tasks import demo_celery_function

# Create your views here.

def celery_test(request):
    try:
        demo_celery_function.apply_async(qyeye="testq")
        return HttpResponse("Here is the celery task!")
    except Exception as e:
        return HttpResponse(str(e))
