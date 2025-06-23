from flask_restful import Resource
from server.models.episode import Episode
from server.app import db

class EpisodeList(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [ep.to_dict() for ep in episodes], 200

class EpisodeDetail(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found."}, 404
        return episode.to_dict(), 200

    def delete(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {"error": "Episode not found."}, 404

        db.session.delete(episode)
        db.session.commit()
        return {}, 204
