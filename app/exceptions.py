class PlanetIdNotFound(LookupError):
    """Raised when a planet id is not between 1 and 8"""

    def __init__(self, planet_id: int):
        super().__init__(f"Planet with id {planet_id} not found")


class InvalidDateTime(ValueError):
    """Raised when a datetime doesn´t follow the format MM/DD/YYYY HH:MM:SS"""

    def __init__(self, datetime: str):
        super().__init__(f"Datetime {datetime} is invalid")
