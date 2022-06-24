from django.http import HttpResponse
from .task import send_mail_task, sleepy
from .helper import *

def index(request):
    # send_mail_without_celery()
    send_mail_task.delay()
    # sleepy.delay(10)
    return HttpResponse('<h1> hello from  celery</h1>')