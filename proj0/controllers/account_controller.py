from flask import jsonify, request

from exceptions.insufficient_funds import InsufficientFunds
from exceptions.user_not_found import UserNotFound
from models.account import Account
from services.account_services import AccountServices
from services.client_services import ClientServices


def route(app):
    @app.route("/clients/<client_id>/accounts", methods=['GET'])
    def get_all_accounts(client_id):
        try:
            if ClientServices.get_client_by_id(client_id):
                return jsonify(AccountServices.all_accounts(client_id)), 200

        except UserNotFound as e:
            return "No such client exists", 404

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['GET'])
    def get_account(account_id, client_id):
        try:
            if ClientServices.get_client_by_id(client_id):
                account = AccountServices.get_account_by_id(int(account_id), client_id)
                return jsonify(account.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except UserNotFound:
            return "No such account or client exists", 404

    @app.route("/clients/<client_id>/accounts", methods=['GET'])
    def get_account_balance_range(client_id):
        if ClientServices.get_client_by_id(client_id):
            balance = request.args["balance"]
            print(balance)
            accounts = AccountServices.get_account_balance_range(float(balance), client_id)
            return jsonify(accounts)
        else:
            return UserNotFound("No such client exists"), 404

    @app.route("/clients/<client_id>/accounts", methods=['POST'])
    def post_account(client_id):

        if ClientServices.get_client_by_id(client_id):
            account = Account.json_parse(request.json)
            account = AccountServices.create_account(account)

            return jsonify(account.json()), 201

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=["PUT"])
    def put_account(account_id, client_id):
        try:
            if ClientServices.get_client_by_id(client_id):
                AccountServices.get_account_by_id(account_id, client_id)
                account = Account.json_parse(request.json)
                account.account_id = int(account_id)
                account = AccountServices.update_account(account, client_id)

                return jsonify(account.json()), 200
        except UserNotFound:
            return "No such account or client exits", 404

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['DELETE'])
    def del_account(account_id, client_id):
        try:
            if ClientServices.get_client_by_id(client_id):
                AccountServices.get_account_by_id(account_id, client_id)
                AccountServices.delete_account(int(account_id), client_id)
                return '', 204
        except UserNotFound:
            return "No such account or client exits", 404

    @app.route("/clients/<client_id>/accounts/<account_id>", methods=['PATCH'])
    def patch_account(account_id, client_id):
        action = request.json['deposit']
        print(action)

        if action == 'deposit' or action == 'withdraw':
            try:
                balance = AccountServices.deposit(
                    int(account_id), client_id) if action == 'deposit' else AccountServices.withdraw(int(account_id), client_id)
                return f"Successful. Balance: {balance}", 200
            except InsufficientFunds:
                return "Insufficient Funds", 422
            except UserNotFound:
                return "No such client or account exists", 404
