from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.individual import IndividualTable
from src.models.sqlite.interfaces.individual_repository import IndividualRepositoryInterface

class IndividualRepository(IndividualRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert_individual(self,full_name: str, age: int, phone_number: str, email: str, category: str, monthly_income: float, balance: float) -> None:
        with self.__db_connection as database:
            try:
                individual_data = IndividualTable(
                    full_name=full_name,
                    age=age,
                    phone_number=phone_number,
                    email=email,
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
                        .one()
                )
                return individual
            except NoResultFound:
                return None

    def update_individual(self, individual_id: int, monthly_income: float, balance: float) -> None:

        with self.__db_connection as database:
            try:
                individual = (
                    database.session
                    .query(IndividualTable)
                    .filter(IndividualTable.id == individual_id)
                    .one()
                )

                individual.monthly_income = monthly_income
                individual.balance = balance

                database.session.commit()

            except Exception as exception:
                database.session.rollback()
                raise exception
