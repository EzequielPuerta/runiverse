from rest_framework.views import APIView

from brands.models import Brand
from brands.schemas import BrandSchema
from runiverse.common.views import DetailViewMixin, ListViewMixin


class BrandListView(ListViewMixin, APIView):
    model = Brand
    schema = BrandSchema


class BrandDetailView(DetailViewMixin, APIView):
    model = Brand
    schema = BrandSchema
