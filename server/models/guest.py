from server.app import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship

class Guest(db.Model, SerializerMixin):
    __tablename__ = "guests"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    occupation = db.Column(db.String)

    appearances = relationship("Appearance", back_populates="guest")

    serialize_rules = ("-appearances.guest",)
