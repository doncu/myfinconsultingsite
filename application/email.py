from email.mime.text import MIMEText
from flask import render_template
import functools
import smtplib
from config import SMTP_SERVER, SMTP_SENDER, SMTP_PASS, SMTP_RECEIVER, SMTP_PORT

try:
    import uwsgi
    from uwsgidecorators import mule
except ImportError:
    def mule(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        return wrapper


@mule
def send_mail(template, **context):
    email_string = render_template(template, **context)
    msg = MIMEText(email_string, 'html')
    msg['Subject'] = 'Новое обращение с сайта'
    msg['From'] = SMTP_SENDER
    msg['To'] = SMTP_RECEIVER

    smtp = smtplib.SMTP_SSL(host=SMTP_SERVER, port=SMTP_PORT)
    smtp.login(SMTP_SENDER, SMTP_PASS)
    smtp.send_message(msg)
    smtp.quit()
