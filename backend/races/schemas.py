from marshmallow.fields import UUID, List, Nested
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

from brands.schemas import BrandSchema
from races.models import Distance, Race, RaceEdition, Series, SeriesEdition


class DistanceSchema(SQLAlchemySchema):
    class Meta:
        model = Distance
        load_instance = True
        include_relationships = True

    _id = auto_field()
    kilometers = auto_field()
    race_editions = List(UUID(), dump_only=True)


class RaceSchema(SQLAlchemySchema):
    class Meta:
        model = Race
        load_instance = True

    _id = auto_field()
    full_name = auto_field()
    fixed_date = auto_field()
    series_id = auto_field()


class SeriesSchema(SQLAlchemySchema):
    class Meta:
        model = Series
        load_instance = True

    _id = auto_field()
    name = auto_field()


class RaceEditionSchema(SQLAlchemySchema):
    class Meta:
        model = RaceEdition
        load_instance = True
        include_relationships = True

    _id = auto_field()
    race_id = auto_field()
    year = auto_field()
    date_time = auto_field()
    location = auto_field()
    sponsor_id = auto_field()
    status = auto_field()
    distances = Nested(DistanceSchema, many=True)
    sponsor = Nested(BrandSchema, dump_only=True)


class SeriesEditionSchema(SQLAlchemySchema):
    class Meta:
        model = SeriesEdition
        load_instance = True

    _id = auto_field()
    year = auto_field()
    series_id = auto_field()
