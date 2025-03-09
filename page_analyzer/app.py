import os

from flask import Flask, flash, redirect, render_template, request, session, url_for
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route('/')
def index():
    # flash('Страница успешно добавлена', 'success')
    # flash('Некорректный URL', 'error')
    # flash('Страница уже существует', 'info')
    return render_template(
        '/index.html',
    )

@app.errorhandler(404)
def not_found(error):
    return render_template(
        '/error.html'), 404

@app.route('/urls')
def get_urls():
    return render_template(
        '/urls.html',
    )
    
@app.route('/urls/<id>')
def get_url(id):
    return render_template(
        '/url.html',
        id=id,
    )