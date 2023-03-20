from flask import Flask
from flask import jsonify

from flask_jwt_extended import JWTManager

from .api.user.user_api import user_api
from .api.transactions.transactions_api import transactions_api

from .config import current_config
from .exceptions import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
with app.app_context():
    from .database import db_session

app.config.from_prefixed_env()
app.config.from_object(current_config())


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.errorhandler(ValueError)
def value_error(e: ValueError):
    return jsonify(msg=e.__cause__), 400

@app.errorhandler(BadCredentials)
def bad_credentials(e: BadCredentials):
    return jsonify(msg=str(e)), 401

@app.errorhandler(NoBodyProvided)
def nobody_provided_error():
    return jsonify(msg="No body has been provided"), 400

@app.errorhandler(SQLAlchemyError)
def sqlalchemy_error(e: SQLAlchemyError):
    return jsonify(msg=e._message()), 500

@app.errorhandler(IntegrityError)
def integrity_error(e: IntegrityError):
    return jsonify(msg=e._message()), 400

app.register_blueprint(user_api)
app.register_blueprint(transactions_api)
jwt = JWTManager(app)