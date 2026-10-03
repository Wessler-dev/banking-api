from src.controllers.legal_entity_creator_controller import LegalEntityCreatorControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class LegalEntityFinderView(ViewInterface):
    def __init__(self, controller: LegalEntityCreatorControllerInterface) -> None:
        self.controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_id = http_request.params.get("legal_entity_id")
        body_response = self.controller.find(legal_entity_id)

        return HttpResponse(status_code=200, body=body_response)
