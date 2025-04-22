from typing import Any, ClassVar, Type

from marshmallow import Schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from sqlalchemy.orm.exc import NoResultFound

from runiverse.sqlalchemy import session


class ListViewMixin:
    model: ClassVar[Type[Any]]
    schema: ClassVar[Type[Schema]]

    def get(self, request: Request) -> Response:
        if not hasattr(self, "model") or not hasattr(self, "schema"):
            raise NotImplementedError(
                "Subclasses must define 'model' and 'schema'"
            )
        objects = session.query(self.model).all()
        data = self.schema(many=True).dump(objects)
        return Response(data)


class DetailViewMixin:
    model: ClassVar[Type[Any]]
    schema: ClassVar[Type[Schema]]

    def get(self, request: Request, pk: str) -> Response:
        if not hasattr(self, "model") or not hasattr(self, "schema"):
            raise NotImplementedError(
                "Subclasses must define 'model' and 'schema'"
            )
        try:
            obj = session.query(self.model).filter_by(_id=pk).one()
            data = self.schema().dump(obj)
            return Response(data)
        except NoResultFound:
            return Response(
                {"detail": f"{self.model.__name__} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
