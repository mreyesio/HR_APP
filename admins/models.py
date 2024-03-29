from nurse_app import db

class Admins(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(80))
    email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    is_admin = db.Column(db.Boolean)

    def __init__(self, fullname, email, username, password, is_admin=False):
        self.fullname = fullname
        self.email = email
        self.username = username
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return '<Admin %r>' % self.username

