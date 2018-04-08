from flask import render_template, request, redirect, url_for
from urllib3 import response

from application import email
from application.app import app
from application.app import recaptcha
import json

from config import RECAPTCHA_SITE_KEY, RECAPTCHA_SECRET_KEY


@app.route('/', endpoint='index')
def index_view():
    return render_template('index.html', alias='index')


@app.route('/about/', endpoint='about')
def about_view():
    return render_template('about.html', alias='about')


@app.route('/contacts/', methods=['GET', 'POST'], endpoint='contacts')
def contacts_view():
    msg=''
    showalert = False
    if request.method == 'POST':
        context = dict(
            captcha=request.form.get('g-recaptcha-response'),
            name=request.form.get('name'),
            email=request.form.get('email'),
            tel=request.form.get('tel'),
            company=request.form.get('company'),
            text=request.form.get('text'),
        )
        showalert = True
        if checkRecaptcha(response, RECAPTCHA_SECRET_KEY):
            msg = 'You are human.'
        else:
            msg = 'You are bot.'
        email.send_mail('email.html', **context)
        return redirect(url_for('contacts'))
    else:
        pass
    return render_template("contact.html", alias='contacts')


def checkRecaptcha(response, secretkey):
    url = 'https://www.google.com/recaptcha/api/siteverify?'
    url = url + 'secret=' + secretkey
    url = url + '&response=' + response
    try:
        #jsonobj = json.loads(request.get_json(url).read())
        jsonobj = request.get_json(url).read()
        if jsonobj['success']:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


@app.route('/portfolio/', endpoint='portfolio')
def portfolio_view():
    return render_template('portfolio.html', alias='portfolio')


@app.route('/services/', endpoint='services')
def services_view():
    return render_template('services.html', alias='services')
