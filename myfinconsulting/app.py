from flask import Flask
from flask import request

from flask_babel import Babel
from flask_admin import Admin

from myfinconsulting import db, config
from myfinconsulting import const
from myfinconsulting.common import utils

app = Flask(__name__, template_folder=config.TEMPLATE_PATH, static_folder=config.STATIC_PATH)
app.config.from_object('config')
babel = Babel(app)
admin = Admin(app, name='admin')
app.add_template_global(const.MENU, 'MENU')
app.add_template_global(const.YEAR, name='YEAR')
app.add_template_global(utils.chunks, name='chunks')


@app.teardown_request
def remove_session(*args):
    db.session.rollback()
    db.session.remove()


@babel.localeselector
def get_locale():
    return request.cookies.get('language', 'ru')


from myfinconsulting import views
from myfinconsulting.admin import views
