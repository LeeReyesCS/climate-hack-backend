from app import db

class Recycler(db.Model):
    recycler_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String)
    zipcode = db.Column(db.Integer)
    email = db.Column(db.String)
    cans = db.Column(db.Integer)
    plastic = db.Column(db.Integer)
    glass = db.Column(db.Integer)


    def to_dict(self):
        return {
            "id":self.recycler_id,
            "name": self.name,
            "zipcode": self.zipcode,
            "email": self.email,
            "cans": self.cans,
            "plastic": self.plastic,
            "glass":self.glass
        }