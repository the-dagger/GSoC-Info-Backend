from app import db

class User(db.Model):
    uid = db.Column(db.String, primary_key=True)
    name = db.Column(db.String, index=True, unique=False)
    email = db.Column(db.String, index=True, unique=True)
    college = db.Column(db.String, index=True, unique=False)
    branch = db.Column(db.String, index=True, unique=False)
    specialization = db.Column(db.String, index=True, unique=False)
    is_mentor = db.Column(db.Boolean, index=True, unique=False)
    cert_link = db.Column(db.String, index=True, unique=True)
    profile_image = db.Column(db.String, index=True, unique=True)
    organization = db.Column(db.String, index=True, unique=False)
    year = db.Column(db.Integer, index=True, unique=False)

    def __repr__(self):
        return '<User %r>' % (self.name)
