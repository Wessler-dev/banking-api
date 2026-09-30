#pylint: disable=unused-argument
from .legal_entity_finder_controller import LegalEntityFinderController

class MockLegalEntity():
    def __init__(self, trade_name, age, phone_number, corporate_email, category, revenue) -> None:
        self.trade_name = trade_name
        self.age = age
        self.phone_number = phone_number
        self.corporate_email = corporate_email
        self.category = category
        self.revenue = revenue

class MockLegalEntityRepository:
    def get_legal_entity(self, legal_entity_id:int):
        return MockLegalEntity(
            trade_name="StarkCorporation",
            age=44,
            phone_number=9770707070,
            corporate_email="StarkCorporation@gmail.com",
            category="Pessoa Juridica",
            revenue=90000000
        )

def test_find():
    controller  = LegalEntityFinderController(MockLegalEntityRepository())
    response = controller.find(123)

    excpected_response = {
        "data": {
            "type": "legal_entity",
            "count": 1,
            "attributes":{
                "trade_name": "StarkCorporation",
                "age": 44,
                "phone_number": 9770707070,
                "corporate_email": "StarkCorporation@gmail.com",
                "category": "Pessoa Juridica",
                "revenue": 90000000                 
            }
        }
    }

    assert response == excpected_response
