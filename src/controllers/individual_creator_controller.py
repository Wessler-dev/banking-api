from typing import Dict
import re
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interfaces.individual_repository import IndividualRepositoryInterface
from .interfaces.individual_creator_controller import IndividualCreatorControllerInterface

class IndividualCreatorController(IndividualCreatorControllerInterface):
    def __init__(self, individual_repository: IndividualRepositoryInterface) -> None:
        self.__individual_repository  = individual_repository

    def create(self, individual_info: Dict) -> Dict:
        full_name = individual_info["full_name"]
        age = individual_info["age"]
        phone_number = individual_info["phone_number"]
        email = individual_info["email"]
        category = individual_info["category"]
        monthly_income = individual_info["monthly_income"]
        balance = individual_info["balance"]

        self.__validade_full_name(full_name)
        self.__insert_individual_in_db(full_name, age, phone_number, email, category, monthly_income, balance)
        formated_response = self.__format_response(individual_info)
        return formated_response

    def __validade_full_name(self, full_name: str) -> None:

        non_valid_caracteres = re.compile(r'[^a-zA-Z]')

        if non_valid_caracteres.search(full_name):
            raise HttpBadRequestError("Nome invalido!")

    def __insert_individual_in_db(self, full_name:str, age:int, phone_number:int, email:str, category:int, monthly_income:int, balance:int) -> None:
        self.__individual_repository.insert_individual(full_name, age, phone_number, email, category, monthly_income,balance)

    def __format_response(self, individual_info: Dict) -> Dict:
        return {
            "data": {
                "type": "individual",
                "count": 1,
                "attributes": individual_info
            }
        }
