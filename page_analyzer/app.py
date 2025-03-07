import os

from flask import Flask, flash, redirect, render_template, request, url_for
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


@app.route('/')
def index():
    return render_template(
        '/index.html',
    )

@app.errorhandler(404)
def not_found(error):
    return render_template(
        '/error.html') , 404