from django.core.mail import EmailMessage
from phone_book.celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task(name='send')
def send(mail_subject, to_email, message):

    email = EmailMessage(
        mail_subject, message, to=[to_email]
    )
    email.send()
    return "Email Sent"


