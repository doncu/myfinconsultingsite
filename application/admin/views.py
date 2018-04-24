from flask_admin.contrib import sqla

import wtforms
from wtforms import validators

from application import db
from application.app import admin
from application.common import utils
from application.admin import fields
from application import models


class AdminModelView(sqla.ModelView):
    def __init__(self, model=None, title=None, category=None, endpoint=None, url=None):
        super().__init__(model or self.__model__, db.session, title, category, endpoint, url)


def register(title=None, url=None, endpoint=None, **kwargs):
    def decorator(cls):
        view = cls(title=title, url=url, endpoint=endpoint, **kwargs)
        cls.instance = view
        admin.add_view(view)
        return cls

    return decorator


@register('Статьи', 'Статьи', '/admin/articles/')
class Catalog(AdminModelView):
    __model__ = models.Articles

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title', 'annotation')
    column_labels = dict(title='Заголовок', annotation='Текст статьи')

    form_columns = ('title', 'annotation')
    form_args = dict(
        title=dict(label='Название статьи', validators=[validators.DataRequired()]),
        annotation=dict(label='Текст статьи', validators=[validators.DataRequired()])
    )
    form_overrides = dict(title=wtforms.StringField, glyphicon=wtforms.StringField, annotation=fields.CKTextAreaField)

    def on_model_change(self, form, model, is_created):
        super().on_model_change(form, model, is_created)
        model.alias = utils.transliterate(model.title)

    def get_query(self):
        query = super().get_query()
        return query
