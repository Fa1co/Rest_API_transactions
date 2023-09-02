from .auth import Authorization
from .transaction import TransactionsApi, TransactionApi


def initialize_routes(api):
    api.add_resource(Authorization, '/api/auth/signup')

    api.add_resource(TransactionsApi, '/api/transactions')
    api.add_resource(TransactionApi, '/api/transaction')