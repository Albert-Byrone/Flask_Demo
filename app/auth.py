from flask import request, jsonify, make_response
from . import db
from .models import User, Profile, Post
from flask_restful import Resource,reqparse
from flask_jwt_extended import create_access_token


register_parser = reqparse.RequestParser()
register_parser.add_argument('username', required=True)
register_parser.add_argument('email', required=True)
register_parser.add_argument('password', required=True)



login_parser = reqparse.RequestParser()
login_parser.add_argument('username', required=True)
login_parser.add_argument('password', required=True)


class Register(Resource):
  def post(self):
    args =register_parser.parse_args()

    # Check if the usernae already exist
    if User.query.filter_by(username=args["username"]).first():
      return {"message": "Username already taken" },400

    if User.query.filter_by(email=args["email"]).first():
      return {"message": "Email already taken" },400

    user = User(username=args["username"], email=args["email"])
    user.set_password(password =args["password"])
    db.session.add(user)
    db.session.commit()
    return { "message": "User created successfully"}, 201

    # Create the use


class Login(Resource):
  def post(self):
    args =login_parser.parse_args()
    # Check if the usernae already exist
    user = User.query.filter_by(username=args["username"]).first()
    resp = make_response("Cookie Set")
    resp.set_cookie('user', user)
    if user and user.check_password(args["password"]):
      access_token = create_access_token(identity=user.username)
      return{"access_token": access_token, "user": { "id": user.id, "username": user.username}},200
    return { "message": "Invalid credentials"}, 401

    # Create the user



def register_user_resources(api):
  api.add_resource(Register, '/register')
  api.add_resource(Login, '/login')

  # Cookes and Sessions


