from typing import Dict
from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.legal_entity_finder_controller import LegalEntityFinderControllerInterface

class LegalEntityFinderController(LegalEntityFinderControllerInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepositoryInterface) -> None:
        self.__legal_entity_repository = legal_entity_repository

    def find(self, legal_entity_id:int) -> Dict:
        legal_entity = self.__find_legal_entity_in_db(legal_entity_id)
        response = self.__format_resposne(legal_entity)
        return response

    def __find_legal_entity_in_db(self, legal_entity_id:int) -> LegalEntityTable:
        legal_entity = self.__legal_entity_repository.get_legal_entity(legal_entity_id)
        if not legal_entity:
            raise HttpNotFoundError("Pessoa Juridica não encontrada!")

        return legal_entity

    def __format_resposne(self, legal_entity: LegalEntityTable) -> Dict:
        return{
            "data": {
                "type": "legal_entity",
                "count": 1,
                "attributes":{
                    "trade_name": legal_entity.trade_name,
                    "age": legal_entity.age,
                    "phone_number": legal_entity.phone_number,
                    "corporate_email": legal_entity.corporate_email,
                    "category": legal_entity.category,
                    "revenue": legal_entity.revenue
                }
            }
        }
