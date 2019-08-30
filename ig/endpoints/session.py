import base64

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

from .apirequest import APIRequest


class Encryption(APIRequest):
    """
        Obtain encryption key to use in order to send the user password in an encrypted form
    """

    ENDPOINT = "/session/encryptionKey"

    def __init__(self):
        super(Encryption, self).__init__(self.ENDPOINT)


class Session(APIRequest):
    """
        Creates a trading session, obtaining session tokens for subsequent API access.
    """

    ENDPOINT = "/session"
    METHOD = "POST"
    EXTRA_HEADERS = {"VERSION": "2"}
    RESPONSE_HEADERS = ["CST", "X-SECURITY-TOKEN"]

    def __init__(
        self,
        identifier: str,
        password: str,
        encryption_key: str,
        encryption_timestamp: int,
    ):
        super(Session, self).__init__(
            endpoint=self.ENDPOINT, method=self.METHOD, header=self.EXTRA_HEADERS
        )

        decoded = base64.b64decode(encryption_key)
        rsakey = RSA.importKey(decoded)

        password_timestamp = password + "|" + str(encryption_timestamp)

        input = base64.b64encode(password_timestamp.encode("UTF-8"))
        encrypted_password = base64.b64encode(  # type: ignore
            PKCS1_v1_5.new(rsakey).encrypt(input)  # type: ignore
        )  # type: ignore

        self.data = {
            "identifier": identifier,
            "password": encrypted_password.decode(),
            "encryptedPassword": True,
        }
