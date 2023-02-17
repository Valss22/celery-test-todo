from django.core.mail import send_mail

from config.settings import EMAIL_HOST
from config.celery import app


@app.task
def send_email_task(subject: str, message: str, email_recipient: list[str]):
    send_mail(subject, message, EMAIL_HOST, email_recipient, fail_silently=False)
