from ..definitions.markets import MarketDetailsFilter, PriceResolution
from .apirequest import APIRequest


class SearchMarkets(APIRequest):
    """
        Returns all markets matching the search term.
    """

    ENDPOINT = "/markets"
    EXTRA_HEADERS = {"VERSION": "1"}

    def __init__(self, search_term: str):
        super(SearchMarkets, self).__init__(
            endpoint=self.ENDPOINT, header=self.EXTRA_HEADERS
        )

        self.params = {"searchTerm": search_term}


class Markets(APIRequest):
    """
        Returns the details of the given markets.

        :epics: The epics of the market to be retrieved, separated by a comma.
        :filter: Filter for the market details: ALL (default) or SNAPSHOT_ONLY
    """

    ENDPOINT = "/markets"
    EXTRA_HEADERS = {"VERSION": "2"}

    def __init__(self, epics: str, filter: str = MarketDetailsFilter.All):
        super(Markets, self).__init__(endpoint=self.ENDPOINT, header=self.EXTRA_HEADERS)

        self.params = {"epics": epics, "filter": filter}


class MarketEpicDetails(APIRequest):
    """
        Returns the details of the given epic.
    """

    ENDPOINT = "/markets/{epic}"
    EXTRA_HEADERS = {"VERSION": "3"}

    def __init__(self, epic: str):
        endpoint = self.ENDPOINT.format(epic=epic)

        super(MarketEpicDetails, self).__init__(
            endpoint=endpoint, header=self.EXTRA_HEADERS
        )


class MarketPrices(APIRequest):
    """
        Returns historical prices for a particular instrument. By default returns the minute prices within the last 10 minutes.

        :from_date - Start date time (yyyy-MM-dd'T'HH:mm:ss)
        :to_date - End date time (yyyy-MM-dd'T'HH:mm:ss)
    """

    ENDPOINT = "/prices/{epic}"
    EXTRA_HEADERS = {"VERSION": "3"}

    def __init__(
        self,
        epic: str,
        resolution: str = PriceResolution.Minute,
        from_date: str = None,
        to_date: str = None,
        max_data_points: int = 10,
        page_size: int = 20,
        page_number: int = 1,
    ):
        endpoint = self.ENDPOINT.format(epic=epic)

        super(MarketPrices, self).__init__(endpoint=endpoint, header=self.EXTRA_HEADERS)

        self.params = {
            "resolution": resolution,
            "from": from_date,
            "to": to_date,
            "max": max_data_points,
            "pageSize": page_size,
            "pageNumber": page_number,
        }
