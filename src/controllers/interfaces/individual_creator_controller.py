from typing import Dict
from abc import ABC, abstractmethod

class IndividualCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self,individual_info: Dict) -> Dict:
        pass
