from models.account import Account


class TempDB:

    accounts = {
        1: Account(account_id=1, client_id=1, balance=100.00),
        2: Account(account_id=2, client_id=2, balance=1000.00)
    }