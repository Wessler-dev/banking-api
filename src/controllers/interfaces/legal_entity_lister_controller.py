from typing import Dict
from abc import ABC, abstractmethod

class LegalEntityListerControllerInterface(ABC):

    @abstractmethod
    def list(self) -> Dict:
        pass
