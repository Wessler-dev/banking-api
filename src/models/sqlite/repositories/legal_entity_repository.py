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
                    .one()
                )
                return legal_entity
            except NoResultFound:
                return None

    def update_legal_entity(self, legal_entity_id:int, revenue:float, balance:float) -> None:

        with self.__db_connection as database:
            try:
                legal_entity= (
                    database.session
                    .query(LegalEntityTable)
                    .filter(LegalEntityTable.id == legal_entity_id)
                    .one()
                )

                legal_entity.revenue = revenue
                legal_entity.balance = balance

                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception
