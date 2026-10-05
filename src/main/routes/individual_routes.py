from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.individual_creator_composer import individual_creator_composer
from src.main.composer.individual_finder_composer import individual_finder_composer
from src.main.composer.individual_lister_composer import individual_lister_composer

from src.errors.error_handler import handle_errors

individual_route_bp = Blueprint("individual_routes", __name__)

@individual_route_bp.route("/individual", methods=["POST"])
def create_individual():
    try:
        http_request = HttpRequest(body=request.json)
        view  = individual_creator_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@individual_route_bp.route("/individual/<individual_id>", methods=["GET"])
def find_individual(individual_id):
    try:
        http_request = HttpRequest(param={"individual_id": individual_id})
        view = individual_finder_composer()

        http_response = view.handle(http_request=http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@individual_route_bp.route("/individual/lister", methods=["GET"])
def list_individual():
    try:
        http_request = HttpRequest()
        view = individual_lister_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
