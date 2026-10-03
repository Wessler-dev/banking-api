from src.controllers.legal_entity_creator_controller import LegalEntityCreatorControllerInterface
from src.validators.legal_entity_creator_validator import legal_entity_creator_validator
from src.views.interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class LegalEntityCreatorView(ViewInterface):
    def __init__(self,controller:LegalEntityCreatorControllerInterface) -> None:
        self.controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        legal_entity_creator_validator(http_request)

        legal_entity_info = http_request.body
        body_response = self.controller.create(legal_entity_info)

        return HttpResponse(status_code=201, body=body_response)
