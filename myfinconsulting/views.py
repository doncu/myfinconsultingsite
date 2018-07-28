import os
import imghdr

from sqlalchemy import orm

from flask import render_template, request, redirect, url_for, send_file

from myfinconsulting import db
from myfinconsulting import models
from myfinconsulting.app import app
from myfinconsulting.common import email


@app.route('/', endpoint='index')
def index_view():
    return render_template('index.html', alias='index')


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
    return render_template('contact.html', alias='contacts')


@app.route('/services/', endpoint='services')
def services_view():
    groups = db.session.query(models.ServiceGroup).options(
        orm.joinedload('services')
    ).order_by(models.ServiceGroup.order).all()
    return render_template('services.html', groups=groups, alias='services')


@app.route('/articles/', endpoint='articles')
def articles_view():
    articles = db.session.query(models.Article).all()
    return render_template('articles.html', articles=articles, alias='articles')


@app.route('/article/<oid>', endpoint='article')
def article_view(oid):
    article = db.session.query(models.Article).filter(models.Article.id == oid).first()
    return render_template('article.html', article=article, alias='article')


@app.route('/privacy-policy/', endpoint='privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html', alias='privacy_policy')


@app.route('/img/<filename>', endpoint='image')
def image_view(filename):
    full_path = os.path.join(app.config['IMG_PATH'], filename)
    type_ = imghdr.what(full_path)
    return send_file(full_path, mimetype='image/{}'.format(type_))
