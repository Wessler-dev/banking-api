from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def individual_creator_validator(http_request: HttpRequest) -> None:

    class BodyData(BaseModel):
        full_name: constr(min_length=1) #type: ignore
        age: int = None
        phone_number: int = None
        email: constr(min_length=1) = None #type: ignore
        category: constr(min_length=1) = None #type: ignore
        monthly_income: int = None

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntityError(e.errors()) from e
