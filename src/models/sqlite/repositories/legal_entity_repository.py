from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.legal_entity import LegalEntityTable
from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface

class LegalEntityRepository(LegalEntityRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_legal_entity(self, trade_name:str, age:int, phone_number:int, corporate_email:str, category:str, revenue:int, balance:float) -> None:
        with self.__db_connection as database:
            try:
                legal_entity_data = LegalEntityTable(
                    trade_name=trade_name,
                      age=age,
                      phone_number=phone_number,
                      corporate_email=corporate_email,
                      category=category,
                      revenue=revenue,
                      balance=balance

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
                        LegalEntityTable.age,
                        LegalEntityTable.phone_number,
                        LegalEntityTable.corportate_email,
                        LegalEntityTable.category,
                        LegalEntityTable.revenue,
                        LegalEntityTable.balance

                    )
                    .one()
                )
                return legal_entity
            except NoResultFound:
                return None
