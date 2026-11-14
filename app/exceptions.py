class HeaderError(Exception):
    def __init__(self, message: str) -> None:
        self._message = message
        super().__init__(self._message)

    @property
    def message(self) -> str:
        return self._message


class AcceptLanguageError(HeaderError):
    pass


class InvalidAcceptLanguageFormatError(AcceptLanguageError):
    pass


class EmptyHeaderError(HeaderError):
    pass


class VersionError(HeaderError):
    pass


class IncorrectVersionFormatError(VersionError):
    pass
