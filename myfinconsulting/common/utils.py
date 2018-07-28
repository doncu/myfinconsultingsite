import babel
from flask import request
from sqlalchemy.ext.hybrid import hybrid_property


def chunks(lst, size):
    """Yield successive size chunks from lst."""
    for i in range(0, len(lst), size):
        yield lst[i:i + size]


def get_locale():
    return request.cookies.get('language', 'ru')


def cast_locale(obj, locale):
    """
    Cast given locale to string. Supports also callbacks that return locales.
    :param obj:
        Object or class to use as a possible parameter to locale callable
    :param locale:
        Locale object or string or callable that returns a locale.
    """
    if callable(locale):
        try:
            locale = locale()
        except TypeError:
            locale = locale(obj)
    if isinstance(locale, babel.Locale):
        return str(locale)
    return locale


class TranslationHybrid:
    def __init__(self, current_locale, default_locale):
        self.current_locale = current_locale
        self.default_locale = default_locale

    def getter_factory(self, **kwargs):
        """
        Return a hybrid_property getter function for given attribute. The
        returned getter first checks if object has translation for current
        locale. If not it tries to get translation for default locale. If there
        is no translation found for default locale it returns None.
        """
        def getter(obj):
            current_locale = cast_locale(obj, self.current_locale)
            attr = kwargs[current_locale]
            return getattr(obj, attr.key)
        return getter

    def setter_factory(self, **kwargs):
        def setter(obj, value):
            locale = cast_locale(obj, self.current_locale)
            attr = kwargs[locale]
            setattr(obj, attr.key, value)
        return setter

    def __call__(self, **kwargs):
        return hybrid_property(fget=self.getter_factory(**kwargs), fset=self.setter_factory(**kwargs))
