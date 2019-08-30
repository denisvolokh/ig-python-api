import logging
import typing

import requests

from .endpoints.apirequest import APIRequest
from .exceptions import APIError, BadEnvironment

ENVIRONMENTS = {
    "DEMO": {"GATEWAY": "https://demo-api.ig.com/gateway/deal"},
    "LIVE": {"DATA": "GATEWAY"},
}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ig.api")


class IGAPI(object):
    def __init__(self, apikey: str, environment: str = "DEMO"):
        self.apikey = apikey
        self.environment = environment

        try:
            ENVIRONMENTS[self.environment]
        except KeyError:
            raise BadEnvironment("Environment is incorrect.")

        self._header_cst = dict()  # type: typing.Dict[str, str]
        self._header_x_security_token = dict()  # type: typing.Dict[str, str]

        self.session = requests.Session()

    def __make_request(
        self,
        url: str,
        method: str,
        query_params: dict = None,
        data_params: dict = None,
        headers: dict = None,
    ):

        if headers is None:
            headers = {}

        headers.update({"X-IG-API-KEY": self.apikey})

        if self._header_cst:
            headers.update(self._header_cst)

        if self._header_x_security_token:
            headers.update(self._header_x_security_token)

        response = None

        if method == "GET":
            response = self.session.get(url=url, params=query_params, headers=headers)

        if method == "POST":
            response = self.session.post(url=url, json=data_params, headers=headers)

        if method == "PUT":
            response = self.session.put(url=url, json=data_params, headers=headers)

        return response

    def request(self, endpoint: APIRequest):

        url = f"{ENVIRONMENTS[self.environment]['GATEWAY']}{endpoint}"

        try:
            query_params = getattr(endpoint, "params")

        except AttributeError:
            query_params = {}

        try:
            data_params = getattr(endpoint, "data")

        except AttributeError:
            data_params = {}

        response = self.__make_request(
            url=url,
            method=endpoint.method,
            data_params=data_params,
            query_params=query_params,
            headers=endpoint.header,
        )

        try:
            expected_headers = getattr(endpoint, "RESPONSE_HEADERS")

        except AttributeError:
            expected_headers = list()

        for header_item in expected_headers:
            if header_item not in response.headers.keys():
                raise APIError("Expected header is not present in response.")

            if header_item == "CST":
                self._header_cst = {"CST": response.headers.get("CST")}

                self.session.headers.update(self._header_cst)

            if header_item == "X-SECURITY-TOKEN":
                self._header_x_security_token = {
                    "X-SECURITY-TOKEN": response.headers.get("X-SECURITY-TOKEN")
                }

                self.session.headers.update(self._header_x_security_token)

        content = response.json()
        endpoint.response = response
        endpoint.header = response.headers
        endpoint.status_code = response.status_code

        return content
