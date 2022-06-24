from celery import shared_task
from time import sleep
from django.core.mail import send_mail
from django.http import HttpResponse


@shared_task
def sleepy(duration):
    sleep(duration)
    return None


@shared_task
def send_mail_task():
    send_mail("CELERY WORKED", "CELERY IS COOL", 'bestpeerstest@gmail.com', ['cel@yopmail.com'], fail_silently=False)
    return None