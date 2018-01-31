"""Init for app package."""
from config import Config

from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)

# down here to avoid circular imports
from app import routes, errors
