from typing import Annotated, Any

from pydantic import (
    BaseModel,
    Field,
    field_validator,
    model_validator,
)

from .exceptions import (
    EmptyHeaderError,
    IncorrectVersionFormatError,
    InvalidAcceptLanguageFormatError,
)
from .utils import (
    is_valid_format_accept_language,
    is_valid_format_version,
)

__all__ = ("CommonHeaders", "GreetingResponseScheme", )


MINIMUM_APP_VERSION = "0.0.2"


class CommonHeaders(BaseModel):
    user_agent: Annotated[str, Field(..., examples=["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"], alias="User-Agent")]
    accept_language: Annotated[str, Field(..., examples=["en-US,en;q=0.9,es;q=0.8"], alias="Accept-Language")]
    x_current_version: Annotated[str, Field(..., pattern=r"^\d+\.\d+\.\d+$", alias="X-Current-Version", exclude=True)]

    @model_validator(mode="before")
    @classmethod
    def _validator_empty_values(cls, data: Any):
        headers = {
            "User-Agent": data.get("User-Agent"),
            "Accept-Language": data.get("Accept-Language"),
            "X-Current-Version": data.get("X-Current-Version")
        }

        for header, value in headers.items():
            if not value:
                raise EmptyHeaderError(f"Отсуствует значение в {header}")

        return data

    @field_validator("x_current_version")
    @classmethod
    def _validator_version(cls, value: str) -> str:
        if not is_valid_format_version(value):
            raise IncorrectVersionFormatError("Не верный формат версии")

        current_version_items = tuple(map(int, value.split(".")))
        minimum_app_version_items = tuple(map(int, MINIMUM_APP_VERSION.split(".")))

        if current_version_items < minimum_app_version_items:
            raise ValueError("Текущая версия приложения устарела! Обновите приложение")

        return value

    @field_validator("accept_language")
    @classmethod
    def _validator_accept_language(cls, value: str) -> str:
        if not is_valid_format_accept_language(value):
            raise InvalidAcceptLanguageFormatError("Неверный формат Accept-Language")

        return value


class GreetingResponseScheme(BaseModel):
    message: str
    headers: CommonHeaders
