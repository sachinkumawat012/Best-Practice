from django.core.mail import send_mail
# Create your views here.

    
def send_mail_without_celery():
    send_mail("CELERY WORKED",
        "CELERY IS COOL",
        'bestpeerstest@gmail.com',
        ['cel@yopmail.com'],
        fail_silently=False
        )
    return None
