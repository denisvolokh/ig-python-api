import logging
import os

import betamax
import pytest
from betamax_serializers import pretty_json

from ig.api import IGAPI
from ig.endpoints.payloads.positions import Position
from ig.endpoints.session import Encryption, Session

betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = "ig/tests/integration/cassettes"
    config.default_cassette_options["serialize_with"] = "prettyjson"


IDENTIFIER = os.getenv("IG__IDENTIFIER", None)
PASSWORD = os.getenv("IG__PASSWORD", None)
APIKEY = os.getenv("IG__APIKEY", None)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ig.tests.conftest")


@pytest.fixture
def identifier():
    return IDENTIFIER


@pytest.fixture
def password():
    return PASSWORD


@pytest.fixture(scope="session")
# @pytest.fixture()
def ig_api_demo_client():
    """
        Returns a IG API instance for DEMO environment
    """

    logger.info("[+] Fixture 'IG API DEMO CLIENT'")

    api_client = IGAPI(apikey=APIKEY, environment="DEMO")

    encryption_endpoint = Encryption()
    encryption_response = api_client.request(encryption_endpoint)
    encryption_key, timestamp = (
        encryption_response["encryptionKey"],
        encryption_response["timeStamp"],
    )

    session_endpoint = Session(
        identifier=IDENTIFIER,
        password=PASSWORD,
        encryption_key=encryption_key,
        encryption_timestamp=timestamp,
    )

    api_client.request(session_endpoint)

    return api_client


@pytest.fixture
def market_position():
    return Position(
        epic="CS.D.GBPUSD.CSD.IP",
        direction="BUY",
        size=10000,
        order_type="MARKET",
        currency_code="USD",
        guaranteed_stop=False,
        force_open=True,
    )


# @pytest.fixture
# def encryption():
#     api_client = IGAPI(apikey=APIKEY, environment="DEMO")

#     encryption_endpoint = Encryption()
#     encryption_response = api_client.request(encryption_endpoint)

#     return (encryption_response["encryptionKey"], encryption_response["timeStamp"])
