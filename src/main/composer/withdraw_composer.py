from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_repository import IndividualRepository
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.controllers.withdraw_controller import WithdrawController
from src.views.withdraw_view import WithdrawView
from src.withdraw.withdraw import Withdraw

def withdraw_composer():
    individual_repository = IndividualRepository(db_connection_handler)
    legal_entity_repository = LegalEntityRepository(db_connection_handler)

    use_case = Withdraw(
        individual_repository,
        legal_entity_repository
    )

    controller = WithdrawController(use_case)
    view = WithdrawView(controller)

    return view
