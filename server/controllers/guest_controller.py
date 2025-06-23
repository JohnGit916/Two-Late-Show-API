from flask_restful import Resource
from server.models.guest import Guest

class GuestList(Resource):
    def get(self):
        guests = Guest.query.all()
        return [guest.to_dict() for guest in guests], 200
