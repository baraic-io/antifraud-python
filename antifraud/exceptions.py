class ErrInternalError(Exception):
    """Exception raised when internal error occured."""

    def __init__(self, message: str | None = None):
        self.message = message
        super().__init__(self.message)

class ErrRequestFailed(Exception):
    """Exception raised when a request failed."""

    def __init__(self, url: str | None = None, code: int | None = None, message: str | None = None):
        self.message = message
        super().__init__(self.message)