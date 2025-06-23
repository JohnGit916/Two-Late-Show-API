from server.app import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship

class Episode(db.Model, SerializerMixin):
    __tablename__ = "episodes"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String, nullable=False)
    number = db.Column(db.Integer, nullable=False)

    appearances = relationship("Appearance", back_populates="episode", cascade="all, delete")

    serialize_rules = ("-appearances.episode",)
