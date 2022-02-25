from ma import ma
from models.number import NumberModel


class NumberSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NumberModel
        load_instance = True