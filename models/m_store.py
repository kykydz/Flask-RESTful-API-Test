from db import db

class StoreModel(db.Model):
    __tablename__ = 'stores'

    id      = db.Column(db.Integer, primary_key=True)
    name    = db.Column(db.String(80))

    #do not go to item table and create each object of it
    # make self.items to be a query builder so we can look inside
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def json(self): #dictionary
        return {'id_store': self.id,'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
