from app import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Colum(db.Integer, primary_key=True)
    username = db.Colum(db.String, unique=True, nullable=False)
    password = db.Colum(db.String, nullable=False)
    name = db.Colum(db.String, nullable=False)
    email = db.Colum(db.String, unique=True, nullable=False)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

class Post(db.Model):
    __tablename__ = "bills"

    id = db.Colum(db.Integer, primary_key=True)
    content = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    user = db.relationship(User, foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self):
        return "<Post %r>" % self.id

class Admin(db.Model):
    __tablename__ = "admins"

    id = db.Colum(db.Integer, primary_key=True)
    username = db.Colum(db.String, unique=True, nullable=False)
    password = db.Colum(db.String, nullable=False)
    name = db.Colum(db.String, nullable=False)
    email = db.Colum(db.String, unique=True, nullable=False)

    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    def __repr__(self):
        return "<Admin %r>" % self.username
