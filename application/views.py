from flask import render_template

from application.app import app


@app.route('/', endpoint='index')
def index_view():
    return render_template('index.html', alias='index')


@app.route('/about/', endpoint='about')
def about_view():
    return render_template('about.html', alias='about')


@app.route('/contacts/', endpoint='contacts')
def contacts_view():
    return render_template("contact.html", alias='contacts')


@app.route('/portfolio/', endpoint='portfolio')
def portfolio_view():
    return render_template('portfolio.html', alias='portfolio')


@app.route('/services/', endpoint='services')
def services_view():
    return render_template('services.html', alias='services')


@app.route('/test', endpoint="test")
def test_view():
    return render_template('test.html')