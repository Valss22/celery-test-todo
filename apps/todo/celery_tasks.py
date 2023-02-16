from django.core.mail import send_mail
from celery import shared_task

from config.settings import EMAIL_HOST


@shared_task()
def send_email_task(subject: str, message: str, email_recipient: list[str]):
    send_mail(subject, message, EMAIL_HOST, email_recipient)
