from typing import Dict
from abc import ABC, abstractmethod

class LegalEntityFinderControllerInterface(ABC):

    @abstractmethod
    def find(self,legal_entity_id: int) -> Dict:
        pass
