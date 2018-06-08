import datetime as dt
import sqlalchemy as sa

from application import db


class Articles(db.Base):
    __tablename__ = 'articles'

    id = sa.Column(sa.Integer, primary_key=True)
    ctime = sa.Column(sa.DateTime, default=dt.datetime.utcnow)
    title = sa.Column(sa.Text, nullable=False)
    annotation = sa.Column(sa.Text, nullable=False)


class Policies(db.Base):
    __tablename__ = 'policies'

    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.Text, nullable=False)
    annotation = sa.Column(sa.Text, nullable=False)