from rest_framework.exceptions import APIException


class InvalidField(APIException):
    status_code = 400

    def __init__(self, field_name: str):
        super().__init__(
            detail=f"The provided value for '{field_name}' is invalid"
        )


class ConfigurationNotFound(APIException):
    status_code = 404

    def __init__(self, cfg_id: int):
        super().__init__(
            detail=f"Config '{cfg_id}' not found on database"
        )
