from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from .exceptions import (
    EmptyHeaderError,
    IncorrectVersionFormatError,
    InvalidAcceptLanguageFormatError,
)



def register_exceptions_handlers(app: FastAPI) -> None:

    @app.exception_handler(EmptyHeaderError)
    def empty_header_exception_handler(request: Request, exp: EmptyHeaderError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": exp.message}
        )

    @app.exception_handler(IncorrectVersionFormatError)
    def incorrect_version_format_exception_handler(request: Request, exp: IncorrectVersionFormatError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": exp.message}
        )

    @app.exception_handler(InvalidAcceptLanguageFormatError)
    def invalid_accept_language_format_exception_handler(request: Request, exp: InvalidAcceptLanguageFormatError):
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": exp.message}
        )
