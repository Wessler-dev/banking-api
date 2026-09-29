from typing import Dict
from abc import ABC, abstractmethod

class LegalEntityCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self,legal_entity_info: Dict) -> Dict:
        pass
