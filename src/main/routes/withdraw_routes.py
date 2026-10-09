from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.withdraw_composer import withdraw_composer

from src.errors.error_handler import handle_errors

withdraw_route_bp = Blueprint("withdraw_routes", __name__)

@withdraw_route_bp.route("/withdraw", methods=["POST"])
def withdraw():
    try:
        http_request = HttpRequest(body=request.json)
        view = withdraw_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code

    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
