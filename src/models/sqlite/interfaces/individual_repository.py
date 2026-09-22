from abc import ABC, abstractmethod
from src.models.sqlite.entities.individual import IndividualTable

class IndividualRepositoryInterface(ABC):

    @abstractmethod
    def insert_individual(self,full_name:str, monthy_income: float,balance:float, category:str) -> None:
        pass

    @abstractmethod
    def get_individual(self, individual_id: int) -> IndividualTable:
        pass
