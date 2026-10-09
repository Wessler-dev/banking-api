from abc import ABC, abstractmethod
from src.models.sqlite.entities.legal_entity import LegalEntityTable

class LegalEntityRepositoryInterface(ABC):

    @abstractmethod
    def insert_legal_entity(self, trade_name:str, age:int, phone_number:int, corporate_email:str, category:str, revenue:int, balance:float) -> None:
        pass

    @abstractmethod
    def get_legal_entity(self, legal_entity_id: int) -> LegalEntityTable:
        pass

    @abstractmethod
    def update_legal_entity(self, legal_entity_id: int, revenue: float, balance: float) -> None:
        pass
