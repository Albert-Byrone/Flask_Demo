
from . import db

from sqlalchemy import CheckConstraint

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    # age = db.Column(dn.Integer, nullable=False)
    profile = db.relationship('Profile', backref='user', uselist=False)  # 1:1
    posts = db.relationship('Post', backref='author', lazy=True)  # 1:Many

    # __table__arg__ =(
    #     CheckConstraint("age > 0", name= "check_positive_age"),
    # )


    def __repr__(self):
        return f'<User {self.username}>'

#One:One
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bio =db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Profile {self.bio}>'


# One: Many
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.title}>'

# Many: Many