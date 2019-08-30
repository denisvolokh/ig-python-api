import logging
import os

import betamax
import pytest

from ig.endpoints.session import Encryption, Session
from ig.endpoints.accounts import Accounts, AccountPreferences, AccountPreferencesUpdate
from ig.endpoints.positions import Positions

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
        update_account_pref_endpoint = AccountPreferencesUpdate(data=update_account_data)

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

        
