import datetime as dt

import sqlalchemy as sa
from sqlalchemy import orm

from myfinconsulting import db
from myfinconsulting.common import utils


translation_hybrid = utils.TranslationHybrid(utils.get_locale, 'ru')


class Article(db.Base):
    __tablename__ = 'articles'

    id = sa.Column(sa.Integer, primary_key=True)
    ctime = sa.Column(sa.DateTime, default=dt.datetime.utcnow)
    title_ru = sa.Column(sa.Text, nullable=False)
    title_en = sa.Column(sa.Text, nullable=False)
    annotation_ru = sa.Column(sa.Text, nullable=False)
    annotation_en = sa.Column(sa.Text, nullable=False)

    title = translation_hybrid(ru=title_ru, en=title_en)
    annotation = translation_hybrid(ru=annotation_ru, en=annotation_en)


class Policie(db.Base):
    __tablename__ = 'policies'

    id = sa.Column(sa.Integer, primary_key=True)
    title_ru = sa.Column(sa.Text, nullable=False)
    title_en = sa.Column(sa.Text, nullable=False)
    annotation_ru = sa.Column(sa.Text, nullable=False)
    annotation_en = sa.Column(sa.Text, nullable=False)

    title = translation_hybrid(ru=title_ru, en=title_en)
    annotation = translation_hybrid(ru=annotation_ru, en=annotation_en)


class ServiceGroup(db.Base):
    __tablename__ = 'service_groups'

    id = sa.Column(sa.Integer, primary_key=True)
    icon = sa.Column(sa.Text, nullable=False)
    title_ru = sa.Column(sa.Text, nullable=False)
    title_en = sa.Column(sa.Text, nullable=False)
    order = sa.Column(sa.Integer, unique=True, index=True, nullable=False)
    annotation_ru = sa.Column(sa.Text, nullable=False)
    annotation_en = sa.Column(sa.Text, nullable=False)

    services = orm.relationship('Service', backref='group', order_by='Service.order')

    title = translation_hybrid(ru=title_ru, en=title_en)
    annotation = translation_hybrid(ru=annotation_ru, en=annotation_en)

    def __str__(self):
        return self.title_ru


class Service(db.Base):
    __tablename__ = 'services'

    id = sa.Column(sa.Integer, primary_key=True)
    title_ru = sa.Column(sa.Text)
    title_en = sa.Column(sa.Text)
    annotation_ru = sa.Column(sa.Text)
    annotation_en = sa.Column(sa.Text)
    small_card = sa.Column(sa.Boolean, default=False)
    order = sa.Column(sa.Integer, unique=True, index=True, nullable=False)

    group_id = sa.Column(sa.ForeignKey('service_groups.id'))

    title = translation_hybrid(ru=title_ru, en=title_en)
    annotation = translation_hybrid(ru=annotation_ru, en=annotation_en)


class Employee(db.Base):
    __tablename__ = 'employees'

    id = sa.Column(sa.Integer, primary_key=True)
    name_ru = sa.Column(sa.Text, nullable=False)
    name_en = sa.Column(sa.Text, nullable=False)
    position_ru = sa.Column(sa.Text, nullable=False)
    position_en = sa.Column(sa.Text, nullable=False)
    annotation_ru = sa.Column(sa.Text, nullable=False)
    annotation_en = sa.Column(sa.Text, nullable=False)

    image = sa.Column(sa.Text, nullable=False)

    name = translation_hybrid(ru=name_ru, en=name_en)
    position = translation_hybrid(ru=position_ru, en=position_en)
    annotation = translation_hybrid(ru=annotation_ru, en=annotation_en)
