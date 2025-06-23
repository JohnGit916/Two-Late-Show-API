from flask import request
from flask_restful import Resource
from server.models.appearance import Appearance
from server.app import db

class AppearanceList(Resource):
    def post(self):
        data = request.get_json()

        try:
            appearance = Appearance(
                rating=data.get("rating"),
                guest_id=data.get("guest_id"),
                episode_id=data.get("episode_id")
            )

            db.session.add(appearance)
            db.session.commit()

            return appearance.to_dict(), 201

        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400
