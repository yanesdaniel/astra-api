import logging

from flask import Flask

from app.config import config_by_name
from app.routes.health import health_bp
from app.routes.planets import planets_bp


def create_app(config_name="dev"):
    app = Flask("Astra API")

    # Load configuration
    config_class = config_by_name[config_name]
    app.config.from_object(config_class)

    # Set up logging
    logging.basicConfig(
        level=logging.DEBUG if config_class.DEBUG else logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    # Blueprints
    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(planets_bp, url_prefix="/api/planets")

    return app
