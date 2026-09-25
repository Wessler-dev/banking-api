from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.legal_entity import LegalEntityTable
from .legal_entity_repository import LegalEntityRepository

class Mockconnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(LegalEntityTable)],
                    [
                        LegalEntityTable(trade_name="Stark Corporation", category="Pesoa Juridica")
                    ]
                )
            ]
        )
    def __enter__(self): return self
    def __exit__(self, exc_typr, exc_val, exc_tb): pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_insert_legal_entity():
    mock_connection = Mockconnection()
    repository = LegalEntityRepository(mock_connection)

    repository.insert_legal_entity(
        trade_name="Stark Corporation",
        revenue=10000000,
        balance=12500.75,
        category="Pessoa Juridica"
    )

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_get_legal_entity():
    mock_connection = Mockconnection()


    legal_entity_id = 1

    repo = LegalEntityRepository(mock_connection)
    response = repo.get_legal_entity(legal_entity_id)
    print()
    print(response)
