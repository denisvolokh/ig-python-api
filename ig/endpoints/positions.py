from .apirequest import APIRequest

class Positions(APIRequest):
    """
        Returns all open positions for the active account.
    """

    ENDPOINT = "/positions"
    EXTRA_HEADERS = {"VERSION": "2"}

    def __init__(self):
        super(Positions, self).__init__(
            endpoint=self.ENDPOINT, header=self.EXTRA_HEADERS
        )

class CreatePosition(APIRequest):
    """
        Creates an OTC position.
    """

    ENDPOINT = "/positions/otc"
    EXTRA_HEADERS = {"VERSION": "2"}

    def __init__(self, data: dict):
        super(Positions, self).__init__(
            endpoint=self.ENDPOINT, header=self.EXTRA_HEADERS
        )

        self.data = data