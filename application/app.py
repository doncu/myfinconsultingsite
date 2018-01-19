from flask import Flask
from flask import request

from flask_babel import Babel
from flask_admin import Admin

import config
from application import db
from application import const
from application.admin import index
from flask_mail import Mail

app = Flask(__name__, template_folder=config.TEMPLATE_PATH, static_folder=config.STATIC_PATH)
app.config.from_object('config')
admin = Admin(
    app,
    name='admin',
    index_view=index.AdminIndexView(url='/admin/'),
    base_template='admin/master.html',
    template_mode='bootstrap3'
)
babel = Babel(app)
app.add_template_global(const.MENU, 'MENU')
app.add_template_global(const.YEAR, name='YEAR')

mail = Mail(app)


@app.teardown_request
def remove_session(*args):
    db.session.rollback()
    db.session.remove()


@babel.localeselector
def get_locale():
    return request.cookies.get('language', 'ru')


from application import views
from application.admin import views
