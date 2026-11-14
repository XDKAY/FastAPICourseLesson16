import re
from datetime import datetime

__all__ = (
    "is_valid_format_accept_language",
    "is_valid_format_version",
    "server_time",
)


_PATTERN_ACCEPT_LANGUAGE = r"^([a-z]{2}(-[A-Z]{2})?(;q=\d(\.\d+)?)?)(,([a-z]{2}(-[A-Z]{2})?(;q=\d(\.\d+)?)?))*$"
_PATTERN_X_SERVER_VERSION = r"^\d+\.\d+\.\d+$"


def is_valid_format_accept_language(value: str) -> bool:
    return bool(re.fullmatch(_PATTERN_ACCEPT_LANGUAGE, value))


def is_valid_format_version(value: str) -> bool:
    return bool(re.fullmatch(_PATTERN_X_SERVER_VERSION, value))


def server_time() -> str:
    return datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
