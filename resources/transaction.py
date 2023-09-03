from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from flask import jsonify
from models import Transaction


class TransactionsApi(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        engine = create_engine('sqlite:///myDatabase.db')
        transactions_data = []
        with Session(autoflush=False, bind=engine) as db:
            transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()
            for transaction in transactions:
                transactions_data.append(
                    {
                        "transaction_id": transaction.transaction_id,
                        "sum": transaction.transaction_sum,
                        "date": transaction.transaction_date,
                        "category": transaction.transaction_category
                    }
                )

        return jsonify(transactions_data)


class TransactionApi(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        engine = create_engine('sqlite:///myDatabase.db')
        body = request.get_json()

        with Session(autoflush=False, bind=engine) as db:
            transaction = Transaction(
                transaction_sum=body['transaction_sum'],
                transaction_date=body['transaction_date'],
                transaction_category=body['transaction_category'],
                user_id=user_id
            )
            db.add(transaction)
            db.commit()

        return '', 200
