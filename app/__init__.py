from flask import Flask

from app.config import config_by_name


def create_app(config_name="dev"):
    app = Flask("Astra API")

    # Load configuration
    app.config.from_object(config_by_name[config_name])

    # Register Blueprints here

    return app