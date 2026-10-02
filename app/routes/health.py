from flask import Blueprint, current_app, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/ping", methods=["GET"])
def ping():
    """Healthcheck endpoint"""
    current_app.logger.info("Healthcheck endpoint called")
    return jsonify({"status": "success", "message": "pong!"}), 200
