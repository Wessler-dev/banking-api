import pytest
from .individual_creator_controller import IndividualCreatorController

class MockIndividualRepository:
    def insert_individual(self, full_name:str, age:int, phone_number:int, email:str, category:int, monthly_income:int) -> None:
        pass

def test_create():
    individual_infor = {
        "full_name": "TonyStark",
        "age": 44,
        "phone_number": 97707070,
        "email": "TonyStark@gmail.com",
        "category": "Pessoa Fisica",
        "monthly_income": 5000
    }

    controller = IndividualCreatorController(MockIndividualRepository())
    response = controller.create(individual_infor)

    assert response ["data"]["type"] == "individual"
    assert response ["data"]["count"] == 1
    assert response ["data"]["attributes"] == individual_infor

def test_create_error():
    individual_infor = {
        "full_name": "Tony Stark123",
        "age": 44,
        "phone_number": 97707070,
        "email": "TonyStark@gmail.com",
        "category": "Pessoa Fisica",
        "monthly_income": 5000
    }

    controller = IndividualCreatorController(MockIndividualRepository())
    with pytest.raises(Exception):

        controller.create(individual_infor)
