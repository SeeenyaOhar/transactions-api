from flask import Blueprint
from flask import request
from flask import jsonify

from flask_jwt_extended import create_access_token

from .security import BcryptManager

from ...models.models import User

from ...database import db_session

from ..utils import inject_body
from ..utils import remove_id

from ...exceptions import NoBodyProvided
from ...exceptions import BadCredentials

user_api = Blueprint('user_api', __name__)
hash_manager = BcryptManager()


def hash_password(user: dict):
    if 'password' not in user:
        raise BadCredentials("Password is invalid")

    user['password'] = hash_manager.hash(user['password'])


@user_api.route("/api/user", methods=['POST'])
@inject_body
def create_user(user):
    remove_id(user)
    hash_password(user)
    user = User(**user)
    db_session.add(user)
    db_session.commit()
    
    return jsonify(user.id), 200


@user_api.route("/api/user/login", methods=['POST'])
@inject_body
def login(credentials):
    email = credentials.get("email", None)
    password = credentials.get("password", None)
    if email is None or password is None:
        return jsonify({"msg": "Bad username or password"}), 400

    user: User = User.query.filter(User.email == email).first()
    if user is None or not hash_manager.validate(password, user.password):
        return jsonify({"msg": "Incorrect username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token)
