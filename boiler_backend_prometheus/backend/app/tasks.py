from app.lib.util_mail import Email
from celery import Celery

app = Celery('tasks', broker='redis://:devpassword@redis:6379/0')


@app.task
def send_recovery_password(token):
    Email().sendVerificationCode(token=token)

@app.task
def add(x, y):
    return x + y