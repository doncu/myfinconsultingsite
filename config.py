import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.abspath(os.path.join(BASE_PATH, 'templates'))
STATIC_PATH = os.path.abspath(os.path.join(BASE_PATH, 'static'))
BABEL_TRANSLATION_DIRECTORIES = os.path.join(BASE_PATH, 'translations')

IMG_PATH = os.environ.get('IMG_PATH', os.path.join(BASE_PATH, 'images'))
DATABASE_URI = 'sqlite:///{}'.format(os.environ.get('DATABASE_URI', os.path.join(BASE_PATH, 'consulting.db')))

SECRET_KEY = 'adsjdasdasdoasd0as98d0am4m35048m90mcw4fum3h4650439875n4354295132'
SMTP_SERVER = 'smtp.mail.ru'
SMTP_PORT = '465'
SMTP_SENDER = 'contact@myfinconsulting.ru'
# SMTP_RECEIVER = 'yuri.avramenko@myfinconsulting.ru'
SMTP_RECEIVER = 'doncusemen@mail.ru'
SMTP_PASS = 'CrE&SY99wlvj'

BABEL_DEFAULT_LOCALE = 'ru'
