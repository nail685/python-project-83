import os

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

from page_analyzer import database, tools

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
urls_repo = database.UrlsRepository(DATABASE_URL)


@app.errorhandler(404)
def not_found(error):
    return render_template(
        '/error.html'), 404


@app.route('/')
def index():
    url = request.args.get("url", "")
    return render_template("index.html", url=url)


@app.route('/urls')
def get_urls():
    urls = urls_repo.get_all_url()
    return render_template(
        '/urls.html',
        urls=urls
    )


@app.route('/urls/<int:url_id>')
def get_url(url_id):
    url = urls_repo.get_url(url_id)
    check_url = urls_repo.get_all_url_checks(url_id)
    return render_template(
        '/url.html',
        url=url, 
        check_url=check_url,
    )


@app.post('/urls')
def new_url():
    gotten_url = request.form.get("url")
    url = tools.normalize_url(gotten_url)
    if not tools.is_valid(url):
        flash('Некорректный URL', category='error')
        return render_template("index.html", url=gotten_url), 422
    if urls_repo.is_url_exist(url):
        url_id = urls_repo.get_url_id(url)
        flash('Страница уже существует', category='info')
        return redirect(url_for("get_url", url_id=url_id))
    url_id = urls_repo.save_url(url)
    flash("Страница успешно добавлена", category="success")
    return redirect(url_for("get_url", url_id=url_id))    


@app.post('/urls/<url_id>/checks')
def check_url(url_id):
    url = urls_repo.get_url(url_id).get('name')
    response = tools.get_response(url)
    if response is None:
        flash("Произошла ошибка при проверке", category="error")
        return redirect(url_for("get_url", url_id=url_id))
    status_code = tools.get_status_code(response)
    tags = tools.get_tags(response)
    urls_repo.save_url_check(url_id, status_code, tags)
    flash("Страница успешно проверена", category="success")
    return redirect(url_for("get_url", url_id=url_id))
