from src.controllers.individual_finder_controller import IndividualFinderControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class IndividualFinderView(ViewInterface):
    def __init__(self, controller: IndividualFinderControllerInterface) -> None:
        self.controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        individual_id = http_request.params.get("individual_id")
        body_response = self.controller.find(individual_id)

        return HttpResponse(status_code=200, body=body_response)
