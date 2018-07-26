#!/usr/bin/env python3
import os
import click

import sqlalchemy as sa
from flask.cli import FlaskGroup


def create_app(*args):
    from myfinconsulting.app import app
    return app


@click.group(cls=FlaskGroup, create_app=create_app)
@click.option('--debug/--no-debug', default=True, help='Enable/disable debug mode')
def cli(debug):
    os.environ['FLASK_DEBUG'] = '1' if debug else '0'


@cli.command('init-db')
@click.option('--db-uri', help='Path where create db')
def init_db(db_uri):
    import myfinconsulting.models
    from myfinconsulting import db

    engine = sa.create_engine(db_uri) if db_uri else db.engine
    db.Base.metadata.create_all(engine)


if __name__ == '__main__':
    cli()
