import logging
import os

import pytest

from ig.api import IGAPI
from ig.exceptions import APIError, BadEnvironment

logger = logging.getLogger("unit")
logger.setLevel(level=logging.DEBUG)


def test_bad_api_environment_exception():
    with pytest.raises(BadEnvironment):
        IGAPI(apikey="", environment="WRONG ENVIRONMENT")


def test_apikey():
    apikey = os.getenv("IG__APIKEY")

    assert apikey is not None

    client = IGAPI(apikey=apikey)
    assert client.apikey == apikey
