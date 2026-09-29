from typing import Dict
from abc import ABC, abstractmethod

class IndividualFinderControllerInterface(ABC):

    @abstractmethod
    def find(self,individual_info: int) -> Dict:
        pass
