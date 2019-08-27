import logging
import os

import betamax
import pytest

from ig.endpoints.session import Encryption, Session

logger = logging.getLogger("integration")
logger.setLevel(level=logging.DEBUG)


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

    def test_encryption_request(self):
        """
            Verify we can get encryption keys
        """

        encryption_endpoint = Encryption()

        cassette_name = self.generate_cassette_name("encryption_request")
        with self.recorder.use_cassette(cassette_name):
            encryption_response = self.client.request(encryption_endpoint)

        assert encryption_endpoint.status_code == 200
        assert "encryptionKey" in encryption_response
        assert "timeStamp" in encryption_response

    def test_session_request(self, identifier: str, password: str, encryption: tuple):
        encryption_key, timestamp = encryption

        session_endpoint = Session(
            identifier=identifier,
            password=password,
            encryption_key=encryption_key,
            encryption_timestamp=timestamp,
        )

        cassette_name = self.generate_cassette_name("session_request")
        with self.recorder.use_cassette(cassette_name):
            session_response = self.client.request(session_endpoint)

        assert session_endpoint.header == session_endpoint.response.headers
        assert session_endpoint.status_code == session_endpoint.expected_status

        for key in session_endpoint.RESPONSE_HEADERS:
            assert key in session_endpoint.response.headers

    # def test__accounts_list(self):
    #     """
    #         Verify we can get a list of accounts
    #     """

    #     accounts_list_request = Accounts()

    #     cassette_name = self.generate_cassette_name("accounts_list")
    #     with self.recorder.use_cassette(cassette_name):
    #         accounts_list_response = self.client.request(accounts_list_request)
    #         content = accounts_list_response.json()

    #     assert accounts_list_response.status_code == accounts_list_request.expected_status
    #     assert isinstance(accounts_list_request.response, list) == True
    #     assert accounts_list_request.response == content

    # # def test__account_details(self):
    # #     pass

    # def test__failed_account_details(self):
    #     account_id = os.getenv("EXANTE__ACCOUNT_ID", None)

    #     account_summary_request = AccountSummary(
    #         account_id=account_id, currency="USD"
    #     )

    #     cassette_name = self.generate_cassette_name("failed_account_details")
    #     with self.recorder.use_cassette(cassette_name):

    #         with pytest.raises(APIError) as exc_info:
    #             account_summary_response = self.client_no_scopes.request(account_summary_request)
