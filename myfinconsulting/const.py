import time
import collections

from flask_babel import lazy_gettext

MenuItem = collections.namedtuple('MenuItem', 'alias name sub')


MENU = [
    MenuItem(alias='index', name=lazy_gettext('Главная'), sub=[]),
    MenuItem(alias='about', name=lazy_gettext('О нас'), sub=[]),
    MenuItem(alias='services', name=lazy_gettext('Услуги'), sub=[]),
    MenuItem(alias='articles', name=lazy_gettext('Статьи'), sub=[]),
    MenuItem(alias='contacts', name=lazy_gettext('Контакты'), sub=[]),
    # MenuItem(alias='language', name=lazy_gettext('Язык'), sub=[
    #     MenuItem(alias='language', name=lazy_gettext('Русский'), sub=[]),
    #     MenuItem(alias='language', name=lazy_gettext('English'), sub=[]),
    # ])

]

YEAR = time.strftime("%Y")
