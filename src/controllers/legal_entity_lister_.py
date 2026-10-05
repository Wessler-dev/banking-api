from typing import Dict, List
from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from .interfaces.legal_entity_lister_controller import LegalEntityListerControllerInterface

class LegalEntityListerController(LegalEntityListerControllerInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepositoryInterface) -> None:

        self.__legal_entity_repository = legal_entity_repository

    def list_legal_entities(self) -> Dict:

        legal_entities = self.__get_legal_entities_in_db()
        response = self.__format_response(legal_entities)
        return response

    def __get_legal_entities_in_db(self) -> List[LegalEntityTable]:

        legal_entities = self.__legal_entity_repository.list_legal_entities()

        return legal_entities

    def __format_response(self, legal_entities: List[LegalEntityTable]) -> Dict:

        formatted_legal_entities = []
        for legal_entity in legal_entities:
            formatted_legal_entities.append({
                "id": legal_entity.id,
                "trade_name": legal_entity.company_name,
                "phone_number": legal_entity.phone_number,
                "corporate_email": legal_entity.corporate_email,
                "revenue": legal_entity.revenue,
                "category": legal_entity.category
            })
        return {
            "data": {
                "type": "legal_entities",
                "count": len(formatted_legal_entities),
                "attributes": formatted_legal_entities
            }
        }
