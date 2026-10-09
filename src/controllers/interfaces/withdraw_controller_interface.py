from typing import Dict
from abc import ABC, abstractmethod

class WithdrawControllerInterface(ABC):

    @abstractmethod
    def withdraw(self,withdraw_info: Dict) -> Dict:
        pass
