from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest

from src.main.composer.legal_entity_creator_composer import legal_entity_creator_composer
from src.main.composer.legal_entity_finder_composer import legal_entity_finder_composer
from src.main.composer.legal_entity_lister_composer import legal_entity_lister_composer

from src.errors.error_handler import handle_errors

legal_entity_route_bp = Blueprint("legal_entity_routes", __name__)

@legal_entity_route_bp.route("/legalentity", methods=["POST"])
def create_legal_entity():
    try:
        http_request = HttpRequest(body=request.json)
        view = legal_entity_creator_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@legal_entity_route_bp.route("/legalentity/<legalentity_id>", methods=["GET"])
def find_legal_entity(legalentity_id):
    try:
        http_request = HttpRequest(param={"legalentity_id": legalentity_id})
        view = legal_entity_finder_composer()

        http_response = view.handle(http_request=http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code

@legal_entity_route_bp.route("/legalentity/lister", methods=["GET"])
def list_legal_entity():
    try:
        http_request = HttpRequest()
        view = legal_entity_lister_composer()

        http_response = view.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)
        return jsonify(http_response.body), http_response.status_code
