from flask import request
from flask_restplus import Resource, fields

from models.number import NumberModel
from schemas.number import NumberSchema
from server.instance import server

ITEM_NOT_FOUND = "Number not found."

number_ns = server.number_ns
number_schema = NumberSchema()
number_list_schema = NumberSchema(many=True)

# Model required by flask_restplus for expect
item = number_ns.model('Number', {
    'value': fields.String('Number value'),
    'monthyPrice': fields.Integer(0),
    'setupPrice': fields.Integer(0),
    'currency': fields.String('Currency'),
})

class Number(Resource):

    def get(self, id):
        number_data = NumberModel.find_by_id(id)
        if number_data:
            return number_schema.dump(number_data)
        return {'message': ITEM_NOT_FOUND}, 404

    def delete(self, id):
        number_data = NumberModel.find_by_id(id)
        if number_data:
            number_data.delete()
            return '', 204
        return {'message': ITEM_NOT_FOUND}, 404

    @number_ns.expect(item)
    def put(self, id):
        number_data = NumberModel.find_by_id(id)
        number_json = request.get_json()

        if number_data:
            number_data.value = number_json['value']
            number_data.monthyPrice = number_json['monthyPrice']
            number_data.setupPrice = number_json['setupPrice']
            number_data.currency = number_json['currency']
        else:
            number_data = number_schema.load(number_json)

        number_data.save()
        return number_schema.dump(number_data), 200

class NumberList(Resource):
    @number_ns.doc('Get all the Items')
    def get(self):
        return number_list_schema.dump(NumberModel.find_all()), 200

    @number_ns.expect(item)
    @number_ns.doc('Create an Item')
    def post(self):
        number_json = request.get_json()
        number_data = number_schema.load(number_json)

        number_data.save()

        return number_schema.dump(number_data), 201
