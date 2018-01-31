"""Config module for flask app."""
import os


class Config(object):
    """Config class inheriting from object object."""

    SECRET_KEY = os.environ.get('SECRET_KEY', '')
