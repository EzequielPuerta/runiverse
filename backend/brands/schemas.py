from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from brands.models import Brand


class BrandSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Brand
        load_instance = True
