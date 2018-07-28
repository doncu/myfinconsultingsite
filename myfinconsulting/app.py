from flask import Flask

from flask_babel import Babel
from flask_admin import Admin

from myfinconsulting import db
from myfinconsulting import const
from myfinconsulting import config
from myfinconsulting.common import utils

app = Flask(__name__, template_folder=config.TEMPLATE_PATH, static_folder=config.STATIC_PATH)
app.config.from_object('myfinconsulting.config')
babel = Babel(app)
admin = Admin(app, name='admin')
app.add_template_global(const.MENU, 'MENU')
app.add_template_global(const.YEAR, name='YEAR')
app.add_template_global(utils.chunks, name='chunks')
babel.localeselector(utils.get_locale)


@app.teardown_request
def remove_session(*args):
    db.session.rollback()
    db.session.remove()


from myfinconsulting import views
from myfinconsulting.admin import views
