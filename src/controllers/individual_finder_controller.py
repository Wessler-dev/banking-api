from typing import Dict
from src.models.sqlite.interfaces.individual_repository import IndividualRepositoryInterface
from src.models.sqlite.entities.individual import IndividualTable
from src.errors.error_types.http_not_found import HttpNotFoundError
from .interfaces.individual_finder_controller import IndividualFinderControllerInterface

class IndividualFinderController(IndividualFinderControllerInterface):
    def __init__(self, individual_repository: IndividualRepositoryInterface) -> None:
        self.__individual_repository = individual_repository

    def find(self, individual_id:int) -> Dict:
        individual = self.__find_person_in_db(individual_id)
        response  = self.__format_response(individual)
        return response

    def __find_person_in_db(self, individual_id:int) -> IndividualTable:
        individual = self.__individual_repository.get_individual(individual_id)
        if not individual:
            raise HttpNotFoundError("Pessoa Fisica não encontrada!")

        return individual

    def __format_response(self, individual: IndividualTable) -> Dict:
        return{
            "data": {
                "type": "individual",
                "count": 1,
                "attributes":{
                    "full_name": individual.full_name,
                    "age": individual.age,
                    "phone_number": individual.phone_number,
                    "email": individual.email,
                    "category": individual.category,
                    "monthly_income": individual.monthly_income                   
                }
            }
        }
