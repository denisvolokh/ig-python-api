import logging
import os

import pytest

from ig.api import IGAPI
from ig.endpoints.payloads.positions import Position
from ig.exceptions import BadEnvironment

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


def test_position_payload_wrong_order_type():
    with pytest.raises(ValueError):
        Position(
            epic="test",
            direction="BUY",
            size=1000,
            order_type="WRONG ORDER TYPE",
            currency_code="USD",
        )


def test_position_payload_order_type_limit():
    with pytest.raises(ValueError):
        Position(
            epic="test",
            direction="BUY",
            size=1000,
            order_type="LIMIT",
            currency_code="USD",
        )


def test_position_payload_order_type_quote():
    with pytest.raises(ValueError):
        Position(
            epic="test",
            direction="BUY",
            size=1000,
            order_type="QUOTE",
            currency_code="USD",
        )

    with pytest.raises(ValueError):
        Position(
            epic="test",
            direction="BUY",
            size=1000,
            order_type="QUOTE",
            currency_code="USD",
            level="12",
        )
