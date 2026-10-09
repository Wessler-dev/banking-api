from src.models.sqlite.interfaces.individual_repository import IndividualRepositoryInterface
from src.models.sqlite.interfaces.legal_entity_repository import LegalEntityRepositoryInterface


class Withdraw:

    def __init__(
        self,
        individual_repository: IndividualRepositoryInterface,
        legal_entity_repository: LegalEntityRepositoryInterface
    ) -> None:
        self.__individual_repository = individual_repository
        self.__legal_entity_repository = legal_entity_repository

    def withdraw(self, person_id:int, category:str, withdraw_amount: float) -> None:

        if withdraw_amount <=0:
            raise ValueError("Digite um valor válido.")

        if category == "individual":
            individual = self.__individual_repository.get_individual(person_id)

            if individual is None:
                raise ValueError("Pessoa fisica não encontrada")

            if withdraw_amount > individual.monthly_income:
                raise ValueError("Saldo insuficiente")

            new_monthly_income = individual.monthly_income - withdraw_amount

            self.__individual_repository.update_individual(person_id, new_monthly_income, withdraw_amount)

        elif category == "legal_entity":
            legal_entity = self.__legal_entity_repository.get_legal_entity(person_id)

            if legal_entity is None:
                raise ValueError("Pessoa juridica não encontrada.")

            if withdraw_amount > legal_entity.revenue:
                raise ValueError("Saldo insuficiente.")

            new_revenue = legal_entity.revenue - withdraw_amount

            self.__legal_entity_repository.update_legal_entity(person_id, new_revenue, withdraw_amount)

        else:
            raise ValueError("Categoria inválida.")
