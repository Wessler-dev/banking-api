from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.individual_repository import IndividualRepository
from src.controllers.individual_finder_controller import IndividualFinderController
from src.views.individual_finder_view import IndividualFinderView

def individual_finder_composer():
    model = IndividualRepository(db_connection_handler)
    controller = IndividualFinderController(model)
    view = IndividualFinderView(controller)

    return view
