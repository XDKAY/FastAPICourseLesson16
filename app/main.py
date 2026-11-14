from fastapi import FastAPI, Header, Response
from .schemes import CommonHeaders, GreetingResponseScheme
from .utils import server_time
from .exceptions_handlers import register_exceptions_handlers


app = FastAPI()

register_exceptions_handlers(app)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Hello World!"
    }


@app.get("/headers", response_model=CommonHeaders)
def headers_endpont(headers: CommonHeaders = Header()):
    return headers


@app.get("/info", response_model=GreetingResponseScheme)
def info_endpoint(response: Response, headers: CommonHeaders = Header()):
    response.headers["X-Server-Time"] = server_time()

    return GreetingResponseScheme(
        message="Добро пожаловать! Ваши заголовки успешно обработаны.",
        headers=headers
    )
