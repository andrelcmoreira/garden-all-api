from rest_framework.exceptions import APIException


class InvalidField(APIException):
    status_code = 400

    def __init__(self, field_name: str):
        super().__init__(
            detail=f"The provided value for '{field_name}' is invalid"
        )
