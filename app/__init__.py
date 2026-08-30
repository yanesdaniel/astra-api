from flask import Flask

from app.config import config_by_name
from app.routes.health import health_bp
from app.routes.planets import planets_bp


def create_app(config_name="dev"):
    app = Flask("Astra API")

    # Load configuration
    app.config.from_object(config_by_name[config_name])

    # Blueprints
    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(planets_bp, url_prefix="/api/planets")

    return app
