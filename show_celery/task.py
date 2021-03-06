from celery import shared_task
from time import sleep

from django.core.mail import send_mail

@shared_task
def sleepy(duration):
    sleep(duration)
    return None

@shared_task
def send_mail_task():
    send_mail('Celery just worked', "Celery done" ,
              "usernasim272727@gmail.com",
              ['nasimnasimnasim272727@gmail.com'],
              fail_silently= False
              )
    return None
