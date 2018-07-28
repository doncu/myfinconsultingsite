import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
ROOT_PATH = os.path.dirname(BASE_PATH)
TEMPLATE_PATH = os.path.abspath(os.path.join(BASE_PATH, 'templates'))
BABEL_TRANSLATION_DIRECTORIES = os.path.join(BASE_PATH, 'translations')

STATIC_PATH = os.path.abspath(os.path.join(ROOT_PATH, 'static'))
IMG_PATH = os.environ.get('IMG_PATH', os.path.join(ROOT_PATH, 'images'))
DATABASE_URI = 'sqlite:///{}'.format(os.environ.get('DATABASE_URI', os.path.join(ROOT_PATH, 'consulting.db')))

SECRET_KEY = 'adsjdasdasdoasd0as98d0am4m35048m90mcw4fum3h4650439875n4354295132'
SMTP_SERVER = 'smtp.mail.ru'
SMTP_PORT = '465'
SMTP_SENDER = 'contact@myfinconsulting.ru'
# SMTP_RECEIVER = 'yuri.avramenko@myfinconsulting.ru'
SMTP_RECEIVER = 'yuri.avramenko@myfinconsulting.ru'
SMTP_PASS = 'CrE&SY99wlvj'

BABEL_DEFAULT_LOCALE = 'ru'
