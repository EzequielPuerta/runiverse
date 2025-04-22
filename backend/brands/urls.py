from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from brands import views

urlpatterns = [
    path(
        "brands/",
        views.BrandListView.as_view(),
        name="brand-list",
    ),
    path(
        "brands/<uuid:pk>/",
        views.BrandDetailView.as_view(),
        name="brand-detail",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
