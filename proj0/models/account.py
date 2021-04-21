class Account:

    def __init__(self, account_id=0, account_number=0, client_id=0, balance=0, acc_type="", acc_status=""):
        self.account_id = account_id
        self.account_number = account_number
        self.client_id = client_id
        self.balance = balance
        self.acc_type = acc_type
        self.acc_status = acc_status

    def json(self):
        return {
            'accountId': self.account_id,
            'accountNumber': self.account_number,
            'clientId': self.client_id,
            'balance': self.balance,
            'accountType': self.acc_type,
            'accountStatus': self.acc_status
        }

    @staticmethod
    def json_parse(json):
        account = Account()
        account.account_id = json["accountId"]
        account.account_number = json["accountNumber"]
        account.client_id = json["clientId"]
        account.balance = json["balance"]
        account.acc_type = json["accountType"]
        account.acc_status = json["accountStatus"]

        return account

    def __repr__(self):
        return str(self.json())
