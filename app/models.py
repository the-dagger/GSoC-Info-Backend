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

    def __init__(self,uid,name,email,college,branch,specialization,is_mentor,cert_link,profile_image,organization,year):
        self.uid = uid
        self.name = name
        self.branch = branch
        self.cert_link = cert_link
        self.college = college
        self.email = email
        self.is_mentor = is_mentor
        self.organization = organization
        self.profile_image = profile_image
        self.specialization = specialization
        self.year = year
        
    def __repr__(self):
        return '<User %r>' % (self.name)
