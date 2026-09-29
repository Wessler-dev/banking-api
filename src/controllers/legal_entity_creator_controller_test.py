import pytest
from .legal_entity_creator_controller import LegalEntityCreatorController

class MockLegalEntityRepository:
    def insert_legal_entity(self, trade_name:str, age:int, phone_number:int, corporate_email:str, category:str, revenue:int) -> None:
        pass

def test_create():
    legal_entity_infor = {
        "trade_name": "Stark Corporation",
        "age": 44,
        "phone_number": 97707070,
        "corporate_email": "StarkCorporation@gmail.com",
        "category": "Pessoa Juridica",
        "revenue": 5000000
    }

    controller = LegalEntityCreatorController(MockLegalEntityRepository())
    response = controller.create(legal_entity_infor)

    assert response ["data"]["type"] == "legal_entity"
    assert response ["data"]["count"] == 1
    assert response ["data"]["attributes"] == legal_entity_infor

def test_create_error():
    legal_entity_infor = {
        "trade_name": "Stark Corporation123",
        "age": 44,
        "phone_number": 97707070,
        "corporate_email": "StarkCorporation@gmail.com",
        "category": "Pessoa Juridica",
        "revenue": 5000000
    }

    controller = LegalEntityCreatorController(MockLegalEntityRepository())
    with pytest.raises(Exception):

        controller.create(legal_entity_infor)
