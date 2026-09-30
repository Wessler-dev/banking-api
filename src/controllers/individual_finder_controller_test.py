#pylint: disable=unused-argument
from .individual_finder_controller import IndividualFinderController

class MockIndividual():
    def __init__(self, full_name, age, phone_number, email, category, monthly_income) -> None:
        self.full_name = full_name
        self.age = age
        self.phone_number = phone_number
        self.email = email
        self.category = category
        self.monthly_income = monthly_income

class MockIndividualRepository:
    def get_individual(self, individual_id:int):
        return MockIndividual(
            full_name="Tony Stark",
            age=44,
            phone_number=9770707070,
            email="tonystark@gmail.com",
            category="Pessoa Fisica",
            monthly_income=90000
        )

def test_find():
    controller  = IndividualFinderController(MockIndividualRepository())
    response = controller.find(123)

    excpected_response = {
        "data": {
            "type": "individual",
            "count": 1,
            "attributes":{
                "full_name": "Tony Stark",
                "age": 44,
                "phone_number": 9770707070,
                "email": "tonystark@gmail.com",
                "category": "Pessoa Fisica",
                "monthly_income": 90000                  
            }
        }
    }

    assert response == excpected_response
