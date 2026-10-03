from src.validators.legal_entity_creator_validator import legal_entity_creator_validator

class MockRequest:
    def __init__(self,body) -> None:
        self.body = body

def test_legal_entity_creator_validator():
    request = MockRequest({
        "trade_name": "Empresa Teste",
        "age": 300,
        "phone_number": 123456789,
        "corporate_email": "Empresateste@gmail.com",
        "category": "Pessoa Juridica",
        "revenue": 10000000
    })

    legal_entity_creator_validator(request)
