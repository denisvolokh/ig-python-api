import logging

import betamax
import pytest

from ig.definitions.markets import MarketDetailsFilter
from ig.endpoints.accounts import AccountPreferences, AccountPreferencesUpdate, Accounts
from ig.endpoints.clientsentiment import ClientMarketSentiment
from ig.endpoints.markets import MarketEpicDetails, MarketPrices, Markets, SearchMarkets
from ig.endpoints.positions import CreatePosition, Positions

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ig.tests.integration")


class TestSaxoOpenAPI(object):
    """
        Integration tests for the IG API object.
    """

    @pytest.fixture(autouse=True)
    def setup(self, ig_api_demo_client):
        """
            Create IGAPI and Betamax instances.
        """

        self.client = ig_api_demo_client
        self.recorder = betamax.Betamax(session=self.client.session)

    @staticmethod
    def generate_cassette_name(method_name):
        """Generate cassette names for tests."""
        return "ig_api__" + method_name

    def test__session_headers(self):
        assert "CST" in self.client.session.headers.keys()
        assert "X-SECURITY-TOKEN" in self.client.session.headers.keys()

    def test__accounts(self):
        """
            Verify we can get a list of accounts
        """

        accounts_endpoint = Accounts()

        cassette_name = self.generate_cassette_name("accounts_list")
        with self.recorder.use_cassette(cassette_name):
            accounts_response = self.client.request(accounts_endpoint)

        assert "accounts" in accounts_response

    def test__account_preferences(self):
        """
            Verify we can get account preferences
        """

        account_pref_endpoint = AccountPreferences()

        cassette_name = self.generate_cassette_name("account_preferences")
        with self.recorder.use_cassette(cassette_name):
            account_response = self.client.request(account_pref_endpoint)

        assert "trailingStopsEnabled" in account_response

    def test__update_account_preferences(self):
        """
            Verify we can update account preferences
        """

        update_account_data = {"trailingStopsEnabled": True}
        update_account_pref_endpoint = AccountPreferencesUpdate(
            data=update_account_data
        )

        cassette_name = self.generate_cassette_name("update_account_preferences")
        with self.recorder.use_cassette(cassette_name):
            update_account_response = self.client.request(update_account_pref_endpoint)

        assert "status" in update_account_response
        assert update_account_response["status"] == "SUCCESS"

    def test__positions(self):
        """
            Verify we can get all open positions
        """

        positions_endpoint = Positions()

        cassette_name = self.generate_cassette_name("positions")
        with self.recorder.use_cassette(cassette_name):
            positions_response = self.client.request(positions_endpoint)

        logger.info(positions_response)

        assert "positions" in positions_response

    def test__create_otc_market_position(self, market_position):
        """
            Verify we can create market OTC position
        """

        create_position_endpoint = CreatePosition(data=market_position.data)

        cassette_name = self.generate_cassette_name("create_position")
        with self.recorder.use_cassette(cassette_name):
            create_position_response = self.client.request(create_position_endpoint)

        assert "dealReference" in create_position_response

    # Markets endpoints

    def test__search_market(self):
        """
            Verify we can search market for instrument
        """

        search_market_endpoint = SearchMarkets(search_term="USDGBP")

        cassette_name = self.generate_cassette_name("search_markets")
        with self.recorder.use_cassette(cassette_name):
            search_markets_response = self.client.request(search_market_endpoint)

        assert "markets" in search_markets_response
        assert len(search_markets_response["markets"]) > 0

    def test__markets_details(self):
        """
            Verify we can get markets details
        """

        epic = "CS.D.GBPUSD.CSD.IP"

        markets_details_endpoint = Markets(
            epics=epic, filter=MarketDetailsFilter.SnapshotOnly
        )

        cassette_name = self.generate_cassette_name("markets_details")
        with self.recorder.use_cassette(cassette_name):
            markets_details_response = self.client.request(markets_details_endpoint)

        assert "marketDetails" in markets_details_response

    def test__market_epic_details(self):
        """
            Verify we can get market epic details
        """

        epic = "CS.D.GBPUSD.CSD.IP"

        market_epic_details_endpoint = MarketEpicDetails(epic=epic)

        cassette_name = self.generate_cassette_name("market_epic_details")
        with self.recorder.use_cassette(cassette_name):
            market_epic_details_response = self.client.request(
                market_epic_details_endpoint
            )

        assert "instrument" in market_epic_details_response
        assert market_epic_details_response["instrument"]["epic"] == epic

    def test__market_price(self):
        """
            Verify we can get market price for given epic
        """

        epic = "CS.D.GBPUSD.CSD.IP"

        prices_endpoint = MarketPrices(epic=epic)

        cassette_name = self.generate_cassette_name("market_prices")
        with self.recorder.use_cassette(cassette_name):
            prices_response = self.client.request(prices_endpoint)

        assert "prices" in prices_response

    # Client Sentiment endpoints

    def test_client_sentiment(self):
        """
            Verify we can get client sentiment
        """

        market_ids = "FT100,EURUSD"

        client_sentiment_endpoint = ClientMarketSentiment(market_ids=market_ids)

        cassette_name = self.generate_cassette_name("client_sentiment")
        with self.recorder.use_cassette(cassette_name):
            client_sentiment_response = self.client.request(client_sentiment_endpoint)

        assert "clientSentiments" in client_sentiment_response
        assert len(client_sentiment_response["clientSentiments"]) == 2
