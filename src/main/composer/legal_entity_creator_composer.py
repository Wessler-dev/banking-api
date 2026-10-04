from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.legal_entity_repository import LegalEntityRepository
from src.controllers.legal_entity_creator_controller import LegalEntityCreatorController
from src.views.legal_entity_creator_view import LegalEntityCreatorView

def legal_entity_creator_composer():
    model = LegalEntityRepository(db_connection_handler)
    controller = LegalEntityCreatorController(model)
    view = LegalEntityCreatorView(controller)

    return view
