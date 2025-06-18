from flask import request, jsonify
from .models import User, Profile, Post
from flask_restful import Resource,reqparse


# RequestParser
user_parser = reqparse.RequestParser()
user_parser.add_argument('username', required=False)
user_parser.add_argument('email', required=False)


class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return jsonify([
            {
                "id":user.id,
                "username": user.username,
                "email": user.email,
                "profile" : user.profile.bio if user.profile else None,
                "post":[
                    {
                        "id": post.id,
                        "title": post.title,
                        "content": post.content
                    }for post in  user.posts],
            } for user in users
        ])
    def post(self):
        args = user_parser.parse_args
        user =User(username=args["username"], email=args["email"])  # GIve me the validated data
        db.session.add(user)
        db.commit()
        return { "id": user.id }, 201


class UserResource(Resource):
    def get(self,id):
        user = User.query.get_or_404(id)# Single
        return jsonify(
            {
                "id":user.id,
                "username": user.username,
                "email": user.email,
                "profile" : user.profile.bio if user.profile else None,
                "post":[
                    {
                        "id": post.id,
                        "title": post.title,
                        "content": post.content
                    }for post in  user.posts],
            } )

class PostListResource(Resource):
    def get(self):
        posts = Post.query.all()
        return jsonify([
            {
                "id":post.id,
                "title": post.title,
                "content": post.content
            } for post in posts
        ])



def register_resources(api):
    api.add_resource(UserListResource, '/users')
    api.add_resource(PostListResource, '/posts')
    api.add_resource(UserResource, '/users/<int:id>')






