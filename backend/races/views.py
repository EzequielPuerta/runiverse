from rest_framework.views import APIView

from races.models import Distance, Race, RaceEdition, Series, SeriesEdition
from races.schemas import (
    DistanceSchema,
    RaceEditionSchema,
    RaceSchema,
    SeriesEditionSchema,
    SeriesSchema,
)
from runiverse.common.views import DetailViewMixin, ListViewMixin


class DistanceListView(ListViewMixin, APIView):
    model = Distance
    schema = DistanceSchema


class DistanceDetailView(DetailViewMixin, APIView):
    model = Distance
    schema = DistanceSchema


class RaceListView(ListViewMixin, APIView):
    model = Race
    schema = RaceSchema


class RaceDetailView(DetailViewMixin, APIView):
    model = Race
    schema = RaceSchema


class SeriesListView(ListViewMixin, APIView):
    model = Series
    schema = SeriesSchema


class SeriesDetailView(DetailViewMixin, APIView):
    model = Series
    schema = SeriesSchema


class RaceEditionListView(ListViewMixin, APIView):
    model = RaceEdition
    schema = RaceEditionSchema


class RaceEditionDetailView(DetailViewMixin, APIView):
    model = RaceEdition
    schema = RaceEditionSchema


class SeriesEditionListView(ListViewMixin, APIView):
    model = SeriesEdition
    schema = SeriesEditionSchema


class SeriesEditionDetailView(DetailViewMixin, APIView):
    model = SeriesEdition
    schema = SeriesEditionSchema
