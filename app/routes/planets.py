from flask import Blueprint, jsonify, request

from app.controllers.planets_controller import get_planet_by_id
from app.exceptions import InvalidDateTime, PlanetIdNotFound

planets_bp = Blueprint("planets", __name__)


@planets_bp.route("/<int:planet_id>", methods=["GET"])
def get_planet(planet_id):
    try:
        datetime = request.args.get("datetime", "01/01/2000 12:00:00", str)
        result = get_planet_by_id(planet_id, datetime)
        return jsonify(result), 200
    except PlanetIdNotFound as err:
        return jsonify({"error": str(err)}), 404
    except InvalidDateTime as err:
        return jsonify({"error": str(err)}), 400
