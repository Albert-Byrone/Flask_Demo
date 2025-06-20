
from flask_restful import Resource, Api
from flask import jsonify, request
from app import create_app, db
from app.models import User, Profile

app = create_app()
api =Api(app)


@app.before_request
def create_tables():
    db.create_all()

@app.shell_context_processor
def make_shell_context():
    return {'db': db , 'User': User, "Profile": Profile}



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")



# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255))
#     content = db.Column(db.Text)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     profile = db.relationship('Profile', backref='user', uselist=False)  # 1:1
#     posts = db.relationship('Post', backref='author', lazy=True)  # 1:Many

#     def __repr__(self):
#         return f'<User {self.username}>'



# Authentication -Access token
# Authorization