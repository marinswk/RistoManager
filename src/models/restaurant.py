from app import db


class Restaurant(db.Model):
    """
    represent a restaurant entry in the restaurant db table
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    address = db.Column(db.String(140))
    opening_hours = db.Column(db.String(140))
    style = db.Column(db.String(140))
    menu = db.Column(db.String(225))
    is_public = db.Column(db.Boolean, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
