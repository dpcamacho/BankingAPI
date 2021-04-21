from daos.account_dao_impl import AccountDAOImpl
from exceptions.insufficient_funds import InsufficientFunds
from exceptions.user_not_found import UserNotFound
from models.client import Client

from services.client_services import ClientServices


class AccountServices:
    account_dao = AccountDAOImpl()

    @classmethod
    def create_account(cls, account):
        return cls.account_dao.create_account(account)

    @classmethod
    def all_accounts(cls, client_id):
        return cls.account_dao.all_accounts(client_id)

    @classmethod
    def get_account_by_id(cls, account_id, client_id):
        return cls.account_dao.get_account(account_id, client_id)

    @classmethod
    def update_account(cls, account, client_id):
        return cls.account_dao.update_account(account, client_id)

    @classmethod
    def delete_account(cls, account_id, client_id):
        return cls.account_dao.delete_account(account_id, client_id)

    @classmethod
    def get_account_balance_range(cls, balance, client_id):
        accounts = cls.all_accounts(client_id)

        refined_search = []

        for account in accounts:
            if account["balance"] <= balance <= account["balance"]:
                refined_search.append(account)

        return refined_search

    @classmethod
    def deposit(cls, account_id, client_id):
        try:
            account = cls.account_dao.get_account(account_id, client_id)
            amount = float
            account.balance += amount
            cls.update_account(account, client_id)
            return account.balance
        except UserNotFound:
            return "No such account or client exists", 404
        except InsufficientFunds:
            return "Insufficient Funds", 422

    @classmethod
    def withdraw(cls, account_id, client_id):
        try:
            account = cls.account_dao.get_account(account_id, client_id)
            amount = float
            account.balance += amount
            cls.update_account(account, client_id)
            return account.balance
        except UserNotFound:
            return "No such account or client exists", 404
        except InsufficientFunds:
            return "Insufficient Funds", 422
