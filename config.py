import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_PATH = os.path.abspath(os.path.join(BASE_PATH, 'templates'))
STATIC_PATH = os.path.abspath(os.path.join(BASE_PATH, 'static'))
BABEL_TRANSLATION_DIRECTORIES = os.path.join(BASE_PATH, 'translations')

IMG_PATH = os.environ.get('IMG_PATH', os.path.join(BASE_PATH, 'images'))
DATABASE_URI = 'sqlite:///{}'.format(os.environ.get('DATABASE_URI', os.path.join(BASE_PATH, 'consulting.db')))

SECRET_KEY = 'adsjdasdasdoasd0as98d0am4m35048m90mcw4fum3h4650439875n4354295132'

BABEL_DEFAULT_LOCALE = 'ru'
