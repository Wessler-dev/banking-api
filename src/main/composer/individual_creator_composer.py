from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_repository import IndividualRepository
from src.controllers.individual_creator_controller import IndividualCreatorController
from src.views.individual_creator_view import IndividualCreatorView

def individual_creator_composer():
    model = IndividualRepository(db_connection_handler)
    controller = IndividualCreatorController(model)
    view = IndividualCreatorView(controller)

    return view
