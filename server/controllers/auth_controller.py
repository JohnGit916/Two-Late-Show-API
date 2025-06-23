from flask import request
from flask_restful import Resource
from server.models.user import User
from server.app import db
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError

class Register(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        if not username or not password:
            return {"error": "Username and password are required."}, 400

        try:
            user = User(username=username)
            user.password_hash = password  # uses hybrid_property setter

            db.session.add(user)
            db.session.commit()

            return {"message": "User registered successfully."}, 201

        except IntegrityError:
            db.session.rollback()
            return {"error": "Username already exists."}, 409

class Login(Resource):
    def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()

        if user and user.authenticate(password):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200

        return {"error": "Invalid username or password."}, 401
