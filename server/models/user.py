from server.app import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    _password_hash = Column(String, nullable=False)

    serialize_rules = ("-password_hash",)

    @validates("username")
    def validate_username(self, key, value):
        if not value or not isinstance(value, str):
            raise ValueError("Username must be a non-empty string.")
        return value

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Password is write-only.")

    @password_hash.setter
    def password_hash(self, password_plaintext):
        from server.app import bcrypt
        self._password_hash = bcrypt.generate_password_hash(password_plaintext.encode()).decode()

    def authenticate(self, password_plaintext):
        from server.app import bcrypt
        return bcrypt.check_password_hash(self._password_hash, password_plaintext.encode())
