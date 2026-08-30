from flask import Blueprint, jsonify, request

from app.controllers.planets import planets_id_controller
from app.exceptions import InvalidDateTime, PlanetIdNotFound

planets_bp = Blueprint("planets", __name__)


@planets_bp.route("/<int:planet_id>", methods=["GET"])
def planets_id(planet_id):
    try:
        datetime = request.args.get("datetime", "01/01/2000 12:00:00", str)
        result = planets_id_controller(planet_id, datetime)
        return jsonify(result), 200
    except PlanetIdNotFound as err:
        return jsonify({"error": str(err)}), 404
    except InvalidDateTime as err:
        return jsonify({"error": str(err)}), 400
