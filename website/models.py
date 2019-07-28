from app import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filepath = db.Column(db.String(64), index=True, unique=True)
    master_cat = db.Column(db.String(64))
    sub_cat = db.Column(db.String(64))
    article_type = db.Column(db.String(64))
    gender = db.Column(db.String(64))
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Item {}>'.format(self.id)    