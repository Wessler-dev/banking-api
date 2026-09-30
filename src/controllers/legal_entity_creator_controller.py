from typing import Dict
import re
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface
from .interfaces.legal_entity_creator_controller import LegalEntityCreatorControllerInterface

class LegalEntityCreatorController(LegalEntityCreatorControllerInterface):
    def __init__(self, legal_entity_repository: LegalEntityRepositoryInterface) -> None:
        self.__legal_entity_repository = legal_entity_repository

    def create(self, legal_entity_info: Dict) -> Dict:
        trade_name = legal_entity_info["trade_name"]
        age = legal_entity_info["age"]
        phone_number = legal_entity_info["phone_number"]
        corporate_email = legal_entity_info["corporate_email"]
        category = legal_entity_info["category"]
        revenue = legal_entity_info["revenue"]

        self.__validade_trade_name(trade_name)
        self.__insert_legal_entity_in_db(trade_name, age, phone_number, corporate_email, category, revenue)
        formated_response = self.__format_response(legal_entity_info)
        return formated_response

    def __validade_trade_name(self,trade_name:str) -> None:

        non_valid_caracteres = re.compile(r'[^a-zA-Z\s]')

        if non_valid_caracteres.search(trade_name):
            raise HttpBadRequestError("Nome invalido!")

    def __insert_legal_entity_in_db(self, trade_name:str, age:int, phone_number:int, corporate_email:str, category:str, revenue:int) -> None:
        self.__legal_entity_repository.insert_legal_entity(trade_name, age, phone_number, corporate_email, category, revenue)

    def __format_response(self,legal_entity_info: Dict) -> Dict:
        return{
            "data": {
                "type": "legal_entity",
                "count": 1,
                "attributes": legal_entity_info
            }
        }
