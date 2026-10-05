from typing import Dict, List
from src.models.sqlite.interfaces.individual_repository import IndividualRepositoryInterface
from src.models.sqlite.entities.individual import IndividualTable
from .interfaces.individual_lister_controller import IndividualListerControllerInterface

class IndividualListerController(IndividualListerControllerInterface):
    def __init__(self,individual_repository:IndividualRepositoryInterface) -> None:

        self.__individual_repository = individual_repository

    def list(self) -> Dict:

        individuals = self.__get_individuals_in_db()
        response = self.__format_response(individuals)
        return response

    def __get_individuals_in_db(self) -> List[IndividualTable]:

        individuals = self.__individual_repository.list_individuals()

        return individuals

    def __format_response(self, individuals: List[IndividualTable]) -> Dict:

        formatted_individuals = []
        for individual in individuals:
            formatted_individuals.append({
                "id": individual.id,
                "full_name": individual.full_name,
                "phone_number": individual.phone_number,
                "email": individual.email,
                "monthly_income": individual.monthly_income,
                "category": individual.category
            })
        return{
            "data":{
                "type":"individuals",
                "count": len(formatted_individuals),
                "attributes": formatted_individuals
            }
        }
