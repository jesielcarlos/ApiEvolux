from db import db
from typing import List


class NumberModel(db.Model):
    __tablename__ = "numbers"

    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.String(20))
    monthyPrice = db.Column(db.Float(precision=2))
    setupPrice = db.Column(db.Float())
    currency = db.Column(db.String(4))

    def __init__(self, value, monthyPrice, currency, setupPrice):
        self.value = value
        self.monthyPrice = round(monthyPrice, 2)
        self.currency = currency
        self.setupPrice = round(setupPrice, 2)
        
    def __repr__(self):
        return f'NumberModel(id={self.id}, value={self.value})'

    def json(self):
        return {'id': self.id, 'valeu': self.value}

    @classmethod
    def find_by_number(obj, number):
        return obj.query.filter_by(value=number).first()

    @classmethod
    def find_by_id(obj, id):
        return obj.query.filter_by(id=id).first()

    @classmethod
    def find_all(obj):
        return obj.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        