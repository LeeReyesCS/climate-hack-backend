from app import db

class Recycler(db.Model):
    recycler_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    zipcode = db.Column(db.Integer)
    role = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)