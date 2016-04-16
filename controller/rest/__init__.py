# coding=utf-8

from flask import Flask, Blueprint, current_app
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from domain import Base

import importlib
import pkgutil


def create_app(config_name):
    """
    Create Flask application
    :param config_name:
    :return: app
    """

    # Create Flask configuration
    app = Flask(__name__)
    app.config.from_object(config_name)

    # Create cors configuration
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    # Elasticsearch


    # Register blueprints
    register_blueprints(app)

    # SQLAlchemy
    ds_plugin = SQLAlchemy(app)
    SQLAlchemy(app, session_options={
        'autocommit': True,
        'autoflush': False
    })



    # Inserir sempre apos registrar os blueprints
    Base.metadata.create_all(bind=ds_plugin.engine)

    return app


def get_datastore_session():
    """ Retorna o data store configurado.
    """
    return current_app.extensions['sqlalchemy'].db.session


def register_blueprints(app):
    """Registra todos os blueprints em uma aplicação Flask.
    :param app: Flask contato
    """
    package_name = __name__
    package_path = __path__

    register = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        module = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(module):
            item = getattr(module, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            register.append(item)
    return register
