from .apirequest import APIRequest


class Accounts(APIRequest):
    """
        Returns a list of accounts belonging to the logged-in client.
    """

    ENDPOINT = "/accounts"
    EXTRA_HEADERS = {"VERSION": "1"}

    def __init__(self):
        super(Accounts, self).__init__(
            endpoint=self.ENDPOINT, header=self.EXTRA_HEADERS
        )


class AccountPreferences(APIRequest):
    """
        Returns account preferences.
    """

    ENDPOINT = "/accounts/preferences"
    EXTRA_HEADERS = {"VERSION": "1"}

    def __init__(self):
        super(AccountPreferences, self).__init__(
            endpoint=self.ENDPOINT, header=self.EXTRA_HEADERS
        )


class AccountPreferencesUpdate(APIRequest):
    """
        Update account preferences.
    """

    METHOD = "PUT"
    ENDPOINT = "/accounts/preferences"
    EXTRA_HEADERS = {"VERSION": "1"}

    def __init__(self, data: dict):
        super(AccountPreferencesUpdate, self).__init__(
            endpoint=self.ENDPOINT, method=self.METHOD, header=self.EXTRA_HEADERS
        )

        self.data = data
