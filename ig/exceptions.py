class APIError(Exception):
    pass


class BadEnvironment(Exception):
    def __init__(self, message):
        self.message = message

        super(BadEnvironment, self).__init__(message)
