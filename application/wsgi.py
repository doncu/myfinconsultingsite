from werkzeug.contrib import fixers

from application.app import app

app.wsgi_app = fixers.ProxyFix(app.wsgi_app)
