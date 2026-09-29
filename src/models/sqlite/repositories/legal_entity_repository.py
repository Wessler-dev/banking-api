from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface

class LegalEntityRepository(LegalEntityRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_legal_entity(self, trade_name: str, revenue: float, balance: float, category: str) -> None:
        with self.__db_connection as database:
            try:
                legal_entity_data = LegalEntityTable(
                    trade_name=trade_name,
                      revenue=revenue,
                      balance=balance,
                      category=category
                )
                database.session.add(legal_entity_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_legal_entity(self, legal_entity_id:int) -> LegalEntityTable:
        with self.__db_connection as database:
            try:
                legal_entity = (
                    database.session
                    .query(LegalEntityTable)
                    .filter(LegalEntityTable.id ==legal_entity_id)
                    .with_entities(
                        LegalEntityTable.trade_name,
                        LegalEntityTable.revenue,
                        LegalEntityTable.balance,
                        LegalEntityTable.category
                    )
                    .one()
                )
                return legal_entity
            except NoResultFound:
                return None
