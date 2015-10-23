from love_airbnb import db

class Ad(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    dear = db.Column(db.Unicode(25))
    message = db.Column(db.Unicode(270))
    sender = db.Column(db.Unicode(26))

    def __init__(self, dear, message, sender):
        self.dear = dear
        self.message = message
        self.sender = sender

    def __repr__(self):
        return '<Ad (id={0})'.format(self.id)

    def create(self):
        db.session.add(self)
        db.session.commit()

        return self
