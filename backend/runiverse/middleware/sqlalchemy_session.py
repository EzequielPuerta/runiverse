from typing import Callable

from django.http import HttpRequest, HttpResponse

from runiverse.sqlalchemy import SessionLocal


class SQLAlchemySessionMiddleware:
    def __init__(
        self,
        get_response: Callable[[HttpRequest], HttpResponse],
    ) -> None:
        self.get_response = get_response

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            response = self.get_response(request)
            return response
        finally:
            SessionLocal.remove()
