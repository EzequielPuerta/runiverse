from django.urls import path

from races import views

urlpatterns = [
    path(
        "distances/",
        views.DistanceListView.as_view(),
        name="distance-list",
    ),
    path(
        "distances/<uuid:pk>/",
        views.DistanceDetailView.as_view(),
        name="distance-detail",
    ),
    path(
        "race/",
        views.RaceListView.as_view(),
        name="race-list",
    ),
    path(
        "race/<uuid:pk>/",
        views.RaceDetailView.as_view(),
        name="race-detail",
    ),
    path(
        "series/",
        views.SeriesListView.as_view(),
        name="series-list",
    ),
    path(
        "series/<uuid:pk>/",
        views.SeriesDetailView.as_view(),
        name="series-detail",
    ),
    path(
        "race-editions/",
        views.RaceEditionListView.as_view(),
        name="race-edition-list",
    ),
    path(
        "race-editions/<uuid:pk>/",
        views.RaceEditionDetailView.as_view(),
        name="race-edition-detail",
    ),
    path(
        "series-editions/",
        views.SeriesEditionListView.as_view(),
        name="series-edition-list",
    ),
    path(
        "series-editions/<uuid:pk>/",
        views.SeriesEditionDetailView.as_view(),
        name="series-edition-detail",
    ),
]
