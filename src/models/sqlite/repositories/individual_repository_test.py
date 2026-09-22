from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm.exc import NoResultFound

from src.models.sqlite.entities.individual import IndividualTable
from .individual_repository import IndividualRepository

class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(IndividualTable)],
                    [
                        IndividualTable(full_name="Tony Stark",category="Pessoa Fisica")
                    ]
                )
            ]
        )
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass

def test_insert_individual():
    mock_connection = MockConnection()
    repository = IndividualRepository(mock_connection)

    repository.insert_individual(
        full_name="tony Stark",
        monthly_income=10000,
        balance=5000,
        category="Pessoa Fisica"
    )

    mock_connection.session.add.assert_called_once()
    mock_connection.session.commit.assert_called_once()
