"""Routes for personal portfolio site."""
from app import app

from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    """Return index template."""
    return render_template('index.html', title='home')
