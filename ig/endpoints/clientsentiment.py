from .apirequest import APIRequest


class ClientMarketSentiment(APIRequest):
    """
        Returns the client sentiment for the given instrument's market

        :market_ids - Comma separated list of market identifiers
    """

    ENDPOINT = "/clientsentiment"
    EXTRA_HEADERS = {"VERSION": "1"}

    def __init__(self, market_ids: str):

        super(ClientMarketSentiment, self).__init__(
            endpoint=self.ENDPOINT, header=self.EXTRA_HEADERS
        )

        self.params = {"marketIds": market_ids}
