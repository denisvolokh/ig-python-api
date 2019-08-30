class APIRequest(object):

    METHOD = "GET"
    HEADERS = {
        "Content-Type": "application/json; charset=UTF-8",
        "Accept": "application/json; charset=UTF-8",
    }

    def __init__(self, endpoint: str, method: str = "GET", header: dict = None):
        self._endpoint = endpoint

        self._header = self.HEADERS
        if header is not None:
            self._header.update(header)

        self._response = None
        self._status_code = None

        self.method = method

    @property
    def header(self):
        return self._header

    @header.setter
    def header(self, value):
        self._header = value

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    def __str__(self):
        return self._endpoint
