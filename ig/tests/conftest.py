import os

import betamax
import pytest
from betamax_serializers import pretty_json

from ig.api import IGAPI
from ig.definitions.markets import PriceResolution
from ig.endpoints.session import Encryption

betamax.Betamax.register_serializer(pretty_json.PrettyJSONSerializer)

with betamax.Betamax.configure() as config:
    config.cassette_library_dir = "ig/tests/integration/cassettes"
    config.default_cassette_options["serialize_with"] = "prettyjson"


IDENTIFIER = os.getenv("IG__IDENTIFIER", None)
PASSWORD = os.getenv("IG__PASSWORD", None)
APIKEY = os.getenv("IG__APIKEY", None)


@pytest.fixture
def identifier():
    return IDENTIFIER


@pytest.fixture
def password():
    return PASSWORD


@pytest.fixture
def ig_api_demo_client():
    """
        Returns a IG API instance for DEMO environment
    """

    api_client = IGAPI(apikey=APIKEY, environment="DEMO")

    return api_client


@pytest.fixture
def encryption(ig_api_demo_client):
    encryption_endpoint = Encryption()
    encryption_response = ig_api_demo_client.request(encryption_endpoint)

    return (encryption_response["encryptionKey"], encryption_response["timeStamp"])
