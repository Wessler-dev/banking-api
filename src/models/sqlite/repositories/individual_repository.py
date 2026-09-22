from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.individual import IndividualTable
from src.models.sqlite.interfaces.individual_repository import IndividualRepositoryInterface

class IndividualRepository(IndividualRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_individual(self, full_name:str, monthly_income:float, balance:float, category:str) -> None:
        with self.__db_connection as database:
            try:
                individual_data = IndividualTable(
                    full_name=full_name,
                    monthly_income=monthly_income,
                    balance=balance,
                    category=category
                )
                database.session.add(individual_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_individual(self, individual_id: int) -> IndividualTable:
        with self.__db_connection as database:
            try:
                individual = (
                    database.session
                        .query(IndividualTable)
                        .filter(IndividualTable.id == individual_id)
                        .with_entities(
                            IndividualTable.full_name,
                            IndividualTable.monthly_income,
                            IndividualTable.balance,
                            IndividualTable.category
                        )
                        .one()
                )
                return individual
            except NoResultFound:
                return None
