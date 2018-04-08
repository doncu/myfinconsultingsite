from flask import render_template, request, redirect, url_for
from application import email
from application.app import app
from application.app import recaptcha


@app.route('/', endpoint='index')
def index_view():
    return render_template('index.html', alias='index')


@app.route('/about/', endpoint='about')
def about_view():
    return render_template('about.html', alias='about')


@app.route('/contacts/', methods=['GET', 'POST'], endpoint='contacts')
def contacts_view():
    if request.method == 'POST' and recaptcha.verify():
        context = dict(
            name=request.form.get('name'),
            email=request.form.get('email'),
            tel=request.form.get('tel'),
            company=request.form.get('company'),
            text=request.form.get('text'),
        )
        email.send_mail('email.html', **context)
        return redirect(url_for('contacts'))
    else:
        pass
    return render_template("contact.html", alias='contacts')


@app.route('/portfolio/', endpoint='portfolio')
def portfolio_view():
    return render_template('portfolio.html', alias='portfolio')


@app.route('/services/', endpoint='services')
def services_view():
    return render_template('services.html', alias='services')

