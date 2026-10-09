from src.controllers.interfaces.withdraw_controller_interface import WithdrawControllerInterface
from src.views.interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class WithdrawView(ViewInterface):
    def __init__(self, controller:WithdrawControllerInterface) -> None:
        self.controller = controller

    def handle(self, http_request:HttpRequest) -> HttpResponse:

        withdraw_info = http_request.body
        body_response = self.controller.withdraw(withdraw_info)

        return HttpResponse(status_code=200, body=body_response)
