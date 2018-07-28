import os

from flask_admin.form import upload
from flask_admin.contrib import sqla

import wtforms
from wtforms import validators

from myfinconsulting import db
from myfinconsulting import config
from myfinconsulting import models
from myfinconsulting.app import admin
from myfinconsulting.admin import fields


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


@register('Статьи', 'Статьи', '/admin/article/')
class AdminArticlesView(AdminModelView):
    __model__ = models.Article

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title_ru', 'title_en')
    column_labels = dict(title_ru='Заголовок на русском', title_en='Заголовок на английском')

    form_columns = ('title_ru', 'title_en', 'annotation_ru', 'annotation_en')
    form_args = dict(
        title_ru=dict(label='Русское название', validators=[validators.DataRequired()]),
        title_en=dict(label='Английское название', validators=[validators.DataRequired()]),
        annotation_ru=dict(label='Русский текст', validators=[validators.DataRequired()]),
        annotation_en=dict(label='Английский текст', validators=[validators.DataRequired()])
    )
    form_overrides = dict(
        title_ru=wtforms.StringField,
        title_en=wtforms.StringField,
        annotation_en=fields.CKTextAreaField,
        annotation_ru=fields.CKTextAreaField
    )


@register('Политика', 'Политика', '/admin/policy/')
class AdminPoliciesView(AdminModelView):
    __model__ = models.Policie

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title_ru', 'title_en')
    column_labels = dict(title_ru='Заголовок на русском', title_en='Заголовок на английском')

    form_columns = ('title_ru', 'title_en', 'annotation_ru', 'annotation_en')
    form_args = dict(
        title_ru=dict(label='Русское название', validators=[validators.DataRequired()]),
        title_en=dict(label='Английское название', validators=[validators.DataRequired()]),
        annotation_ru=dict(label='Русский текст', validators=[validators.DataRequired()]),
        annotation_en=dict(label='Английский текст', validators=[validators.DataRequired()])
    )
    form_overrides = dict(
        title_ru=wtforms.StringField,
        title_en=wtforms.StringField,
        annotation_en=fields.CKTextAreaField,
        annotation_ru=fields.CKTextAreaField
    )


@register('Группы сервисов', 'Группы сервисов', '/admin/service-group/')
class AdminServiceGroupView(AdminModelView):
    __model__ = models.ServiceGroup

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title_ru', 'title_en', 'order')
    column_labels = dict(title_ru='Заголовок на русском', title_en='Заголовок на английском', order='Порядковый номер')

    form_columns = ('title_ru', 'title_en', 'order', 'icon', 'annotation_ru', 'annotation_en')
    form_args = dict(
        title_ru=dict(label='Русское название', validators=[validators.DataRequired()]),
        title_en=dict(label='Английское название', validators=[validators.DataRequired()]),
        annotation_ru=dict(label='Русский текст', validators=[validators.DataRequired()]),
        annotation_en=dict(label='Английский текст', validators=[validators.DataRequired()]),
    )
    form_overrides = dict(title_ru=wtforms.StringField, title_en=wtforms.StringField, icon=wtforms.StringField)

    def get_query(self):
        return super().get_query().order_by(models.ServiceGroup.order)


@register('Сервис', 'Сервис', '/admin/service/')
class AdminServiceView(AdminModelView):
    __model__ = models.Service

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title_ru', 'title_en')
    column_labels = dict(title_ru='Заголовок на русском', title_en='Заголовок на английском')

    form_columns = ('title_ru', 'title_en', 'annotation_ru', 'annotation_en', 'group', 'image')
    form_args = dict(
        title_ru=dict(label='Русское название', validators=[validators.DataRequired()]),
        title_en=dict(label='Английское название', validators=[validators.DataRequired()]),
        annotation_ru=dict(label='Русский текст', validators=[validators.DataRequired()]),
        annotation_en=dict(label='Английский текст', validators=[validators.DataRequired()]),
        group=dict(label='Группа', validators=[validators.DataRequired()])
    )
    form_overrides = dict(
        title_ru=wtforms.StringField,
        title_en=wtforms.StringField,
        annotation_en=fields.CKTextAreaField,
        annotation_ru=fields.CKTextAreaField
    )

    form_extra_fields = dict(
        image=upload.ImageUploadField(
            label='Картинка',
            base_path=config.IMG_PATH,
            endpoint='image'
        )
    )
