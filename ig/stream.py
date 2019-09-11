import logging

from .lightstreamer import LSClient

logger = logging.getLogger("ig.stream")


class IGStream(object):
    def __init__(self, cst: str, x_security_token: str, lightstreamer_endpoint: str):
        self.cst = cst
        self.x_security_token = x_security_token
        self.lightstreamer_endpoint = lightstreamer_endpoint
        # self.ls_client = None

    def connect(self, account_id: str):
        password = f"CST-{self.cst}|XST-{self.x_security_token}"
        self.ls_client = LSClient(
            self.lightstreamer_endpoint,
            adapter_set="",
            user=account_id,
            password=password,
        )

        try:
            self.ls_client.connect()

        except Exception:
            logger.error("Unable to connect to Lightstreamer Server")

    def unsubscribe_all(self):
        for subcription_key in self.ls_client._subscriptions:
            self.ls_client.unsubscribe(subcription_key)

    def disconnect(self):
        self.unsubscribe_all()
        self.ls_client.disconnect()
