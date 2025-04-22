from typing import Optional

from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(
    request: Request,
    format: Optional[str] = None,
) -> Response:
    return Response(
        {
            "brands": reverse(
                "brand-list",
                request=request,
                format=format,
            ),
            "races": reverse(
                "race-list",
                request=request,
                format=format,
            ),
            "race-editions": reverse(
                "race-edition-list",
                request=request,
                format=format,
            ),
            "series": reverse(
                "series-list",
                request=request,
                format=format,
            ),
            "series-editions": reverse(
                "series-edition-list",
                request=request,
                format=format,
            ),
        }
    )
