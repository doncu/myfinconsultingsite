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
    form_overrides = dict(
        title_ru=wtforms.StringField,
        title_en=wtforms.StringField,
        icon=wtforms.StringField,
        annotation_en=fields.CKTextAreaField,
        annotation_ru=fields.CKTextAreaField
    )

    def get_query(self):
        return super().get_query().order_by(models.ServiceGroup.order)


@register('Сервис', 'Сервис', '/admin/service/')
class AdminServiceView(AdminModelView):
    __model__ = models.Service

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('title_ru', 'title_en')
    column_labels = dict(title_ru='Заголовок на русском', title_en='Заголовок на английском')

    form_columns = ('title_ru', 'title_en', 'annotation_ru', 'annotation_en', 'group', 'order', 'small_card')
    form_args = dict(
        title_ru=dict(label='Русское название'),
        title_en=dict(label='Английское название'),
        annotation_ru=dict(label='Русский текст'),
        annotation_en=dict(label='Английский текст'),
        small_card=dict(label='Маленькая карточка'),
        order=dict(label='Порядковый номер', validators=[validators.DataRequired()]),
        group=dict(label='Группа', validators=[validators.DataRequired()])
    )
    form_overrides = dict(
        title_ru=wtforms.StringField,
        title_en=wtforms.StringField,
        annotation_en=fields.CKTextAreaField,
        annotation_ru=fields.CKTextAreaField
    )


@register('Работники', 'Работники', '/admin/employers/')
class AdminEmployeeView(AdminModelView):
    __model__ = models.Employee

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    column_list = ('name_ru', 'name_en')
    column_labels = dict(name_ru='Имя на русском', name_en='Имя на английском')

    form_columns = (
        'name_ru', 'name_en', 'annotation_ru', 'annotation_en', 'image', 'position_ru', 'position_en'
    )
    form_args = dict(
        name_ru=dict(label='Русское название', validators=[validators.DataRequired()]),
        name_en=dict(label='Английское название', validators=[validators.DataRequired()]),
        annotation_ru=dict(label='Русский текст', validators=[validators.DataRequired()]),
        annotation_en=dict(label='Английский текст', validators=[validators.DataRequired()]),
        position_ru=dict(label='Должность русский', validators=[validators.DataRequired()]),
        position_en=dict(label='Должность английский', validators=[validators.DataRequired()]),
        image=dict(label='Фотография')
    )
    form_overrides = dict(
        name_ru=wtforms.StringField,
        name_en=wtforms.StringField,
        position_ru=wtforms.StringField,
        position_en=wtforms.StringField,
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
