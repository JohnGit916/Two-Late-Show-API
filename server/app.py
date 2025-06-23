from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from server.config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    api = Api(app)

    from server.controllers.auth_controller import Register, Login
    from server.controllers.guest_controller import GuestList
    from server.controllers.episode_controller import EpisodeList, EpisodeDetail
    from server.controllers.appearance_controller import AppearanceList

    api.add_resource(Register, "/register")
    api.add_resource(Login, "/login")
    api.add_resource(EpisodeList, "/episodes")
    api.add_resource(EpisodeDetail, "/episodes/<int:id>")
    api.add_resource(GuestList, "/guests")
    api.add_resource(AppearanceList, "/appearances")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
