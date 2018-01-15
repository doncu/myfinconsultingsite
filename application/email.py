from email.mime.text import MIMEText
from flask import render_template
import functools
import smtplib

try:
    import uwsgi
    from uwsgidecorators import mule
except ImportError:
    def mule(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)

        return wrapper


def send_mail(template, context):
    SENDER = 'doncusemen@ya.ru'
    RECEIVER = 'doncusemen@gmail.com'
    smtp_server = 'smtp.yandex.ru'
    email_string = render_template(template, **context)
    msg = MIMEText(email_string)
    msg['Subject'] = 'Новое обращение с сайта'
    msg['From'] = SENDER
    msg['To'] = RECEIVER

    smtp = smtplib.SMTP(smtp_server)
    smtp.starttls()
    smtp.login('doncusemen@ya.ru', 'kamaser999')
    smtp.send_message(msg)
    smtp.quit()

# send_mail(message=" ".join(fraze))
