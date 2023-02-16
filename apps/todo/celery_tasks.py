from django.core.mail import send_mail
from time import sleep

from celery import shared_task

from config.settings import EMAIL_HOST


@shared_task()
def send_email_task(subject: str, message: str, email_recipient: list[str]):
    sleep(3)  # чисто ради проверки что она не блокирует основной поток
    send_mail(subject, message, EMAIL_HOST, email_recipient)
