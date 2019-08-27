from .apirequest import APIRequest


class ClientMarketsSentiments(APIRequest):
    """
        Returns the client sentiment for the given instrument's market
    """

    ENDPOINT = "/clientsentiment"
    EXTRA_HEADERS = {"VERSION": "1"}

    def __init__(self, market_ids: list):
        super(ClientMarketsSentiments, self).__init__(
            endpoint=self.ENDPOINT, header=self.EXTRA_HEADERS
        )

        self.params = {"marketIds": ",".join(market_ids)}


class ClientMarketSentiment(APIRequest):
    """
        Returns the client sentiment for the given instrument's market
    """

    ENDPOINT = "/clientsentiment/{market_id}"
    EXTRA_HEADERS = {"VERSION": "1"}

    def __init__(self, market_id: str):
        endpoint = self.ENDPOINT.format(market_id)

        super(ClientMarketSentiment, self).__init__(
            endpoint=endpoint, header=self.EXTRA_HEADERS
        )
