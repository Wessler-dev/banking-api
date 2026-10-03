from src.validators.individual_creator_validator import individual_creator_validator

class MockRequest:
    def __init__(self,body) -> None:
        self.body = body

def test_individual_creator_validator():
    request = MockRequest({
        "full_name": "fulano",
        "age": 30,
        "phone_number": 123456789,
        "email": "fulano@gmail.com",
        "category": "Pessoa Física",
        "monthly_income": 10000
    })

    individual_creator_validator(request)
