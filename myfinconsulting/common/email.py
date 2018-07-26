import smtplib
import functools
from email.mime.text import MIMEText

from flask import render_template

from myfinconsulting import config

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
    msg['From'] = config.SMTP_SENDER
    msg['To'] = config.SMTP_RECEIVER

    smtp = smtplib.SMTP_SSL(host=config.SMTP_SERVER, port=config.SMTP_PORT)
    smtp.login(config.SMTP_SENDER, config.SMTP_PASS)
    smtp.send_message(msg)
    smtp.quit()
