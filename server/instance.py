from flask import Flask, Blueprint
from flask_restplus import Api
from marshmallow import ValidationError

from ma import ma
from db import db

class Server():
    def __init__(self):
        self.app = Flask(__name__)
        self.bluePrint = Blueprint('api', __name__, url_prefix='/api')
        self.api = Api(self.bluePrint, doc='/doc', title='Api evolux')
        self.app.register_blueprint(self.bluePrint)

        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['PROPAGATE_EXCEPTIONS'] = True

        self.number_ns = self.number_ns()

        super().__init__()

    def number_ns(self, ):
        return self.api.namespace(name='Numbers', description='number related operations', path='/')

    def run(self, ):
        self.app.run( port=5000, debug=True, host='0.0.0.0')

server = Server()
