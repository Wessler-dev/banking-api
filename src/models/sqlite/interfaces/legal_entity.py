from abc import ABC, abstractmethod
from src.models.sqlite.entities.legal_entity import LegalEntityTable

class LegalEntityTableInterface(ABC):

    @abstractmethod
    def insert_legal_entity(self,trade_name:str, renevue:float, balance:float, category:str) -> None:
        pass

    @abstractmethod
    def get_legal_entity(self, legal_entity_id: int) -> LegalEntityTable:
        pass
