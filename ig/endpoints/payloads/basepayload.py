import json


class BasePayload(object):
    def __init__(self):
        self._data = dict()

    def __repr__(self):
        return json.dumps(self.__dict__)

    @property
    def data(self):
        # Todo: clean data, remove None Key-Values

        return self._data
