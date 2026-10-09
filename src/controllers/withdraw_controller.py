from typing import Dict
from src.withdraw.withdraw import Withdraw
from .interfaces.withdraw_controller_interface import WithdrawControllerInterface


class WithdrawController(WithdrawControllerInterface):
    def __init__(self, withdraw_use_case: Withdraw) -> None:
        self.__withdraw_use_case = withdraw_use_case

    def withdraw(self, withdraw_info: Dict) -> Dict:
        person_id = withdraw_info["id"]
        category = withdraw_info["category"]
        withdraw_amount = withdraw_info["withdraw_amount"]

        self.__withdraw_use_case.withdraw(person_id,category,withdraw_amount)

        return {
            "data": {
                "type": "withdraw",
                "count": 1,
                "attributes": {
                    "id": person_id,
                    "category": category,
                    "balance": withdraw_amount
                }
            }
        }
