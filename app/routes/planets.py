from flask import Blueprint, current_app, jsonify, request

from app.controllers.planets_controller import get_planet_by_id
from app.exceptions import InvalidDateTime, PlanetIdNotFound

planets_bp = Blueprint("planets", __name__)


@planets_bp.route("/<int:planet_id>", methods=["GET"])
def get_planet(planet_id):
    try:
        datetime = request.args.get("datetime", "01/01/2000 12:00:00", str)
        result = get_planet_by_id(planet_id, datetime)
        current_app.logger.info(f"Successfully retrieved planet with ID {planet_id}")
        return jsonify(result), 200
    except PlanetIdNotFound as err:
        current_app.logger.error(f"Planet with ID {planet_id} not found")
        return jsonify({"error": str(err)}), 404
    except InvalidDateTime as err:
        current_app.logger.error(
            f"Invalid datetime format for planet with ID {planet_id}"
        )
        return jsonify({"error": str(err)}), 400
