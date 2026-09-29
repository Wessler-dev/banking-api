import pytest
from src.models.sqlite.settings.connection import db_connection_handler
from .individual_repository import IndividualRepository
from .legal_entity_repository import LegalEntityRepository

#db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interação com o banco")
def test_insert_individual():
    full_name = "Tony Stark"
    monthly_income=10000
    balance=5000
    category  = "Pessoa Fisica"

    repo = IndividualRepository(db_connection_handler)
    repo.insert_individual(full_name, monthly_income, balance, category)

@pytest.mark.skip(reason="interação com o banco")
def test_insert_legal_entity():
    trade_name="Stark Corporation"
    revenue=10000000
    balance=12500.75
    category="Pessoa Juridica"

    repo = LegalEntityRepository(db_connection_handler)
    repo.insert_legal_entity(trade_name, revenue, balance, category)
