from src.controllers.individual_creator_controller import IndividualCreatorControllerInterface
from src.validators.individual_creator_validator import individual_creator_validator
from src.views.interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class IndividualCreatorView(ViewInterface):
    def __init__(self,controller:IndividualCreatorControllerInterface) -> None:
        self.controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        individual_creator_validator(http_request)

        individual_info = http_request.body
        body_response = self.controller.create(individual_info)

        return HttpResponse(status_code=201, body=body_response)
