from flask import Blueprint
from flask import jsonify

from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity

from ...models.models import Transaction
from ...models.models import User

from ...database import db_session

from ..utils import inject_body
from ..utils import remove_id
from ..utils import convert_datetime

transactions_api = Blueprint('transactions_api', __name__)


@transactions_api.route("/api/transaction", methods=['POST'])
@jwt_required()
@inject_body
def create_transaction(transaction):
    remove_id(transaction)
    convert_datetime(key="date", obj=transaction)
    transaction['user_id'] = User.query.filter(User.email == get_jwt_identity()).first().id
    transaction = Transaction(**transaction)
    db_session.add(transaction)
    db_session.commit()

    return jsonify(id=transaction.id), 200


@transactions_api.route("/api/transaction", methods=['GET'])
@jwt_required()
def get_transactions():
    current_user_email = get_jwt_identity()
    current_user = User.query.filter(User.email == current_user_email).first()
    transactions = Transaction.query.filter(Transaction.user == current_user).all()

    return jsonify([i.as_dict() for i in transactions]), 200

