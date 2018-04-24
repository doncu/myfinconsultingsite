from flask import render_template, request, redirect, url_for
from application.common import email
from application.app import app
from application import db
from application import models


@app.route('/', endpoint='index')
def index_view():
    articles = db.session.query(models.Articles).all()
    return render_template('index.html', alias='index', articles=articles)


@app.route('/about/', endpoint='about')
def about_view():
    return render_template('about.html', alias='about')


@app.route('/contacts/', methods=['GET', 'POST'], endpoint='contacts')
def contacts_view():
    if request.method == 'POST':
        context = dict(
            name=request.form.get('name'),
            email=request.form.get('email'),
            tel=request.form.get('tel'),
            company=request.form.get('company'),
            text=request.form.get('text'),
        )
        email.send_mail('email.html', **context)
        return redirect(url_for('contacts'))
    return render_template("contact.html", alias='contacts')


@app.route('/services/', endpoint='services')
def services_view():
    return render_template('services.html', alias='services')


@app.route('/articles/', endpoint='articles')
def articles_view():
    articles = db.session.query(models.Articles).all()
    return render_template('articles.html', alias='articles', articles=articles)


@app.route('/article/<id>')
def article_view(id):
    article = db.session.query(models.Articles).filter(models.Articles.id == id).first()
    return render_template('article.html', alias='article', article=article)
