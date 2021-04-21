from daos.account_dao import AccountDAO
from exceptions.user_not_found import UserNotFound
from models.account import Account
from util.db_connection import connection


class AccountDAOImpl(AccountDAO):

    def create_account(self, account):
        sql = "INSERT INTO accounts VALUES (DEFAULT, DEFAULT, %s, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (account.client_id, account.balance, account.acc_type, account.acc_status))

        connection.commit()
        record = cursor.fetchone()

        new_account = Account(record[0], record[1], record[2], float(record[3]), record[4], record[5])
        return new_account

    def get_account(self, account_id, client_id):
        sql = "SELECT * FROM accounts WHERE account_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])

        record = cursor.fetchone()
        if record:
            return Account(record[0], record[1], record[2], float(record[3]), record[4], record[5])
        else:
            raise UserNotFound(f"Account with id: {account_id} - Not Found")

    def all_accounts(self, client_id):
        sql = "SELECT * FROM accounts WHERE client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, client_id)
        records = cursor.fetchall()

        account_list = []

        for record in records:
            account = Account(record[0], record[1], record[2], float(record[3]), record[4], record[5])

            account_list.append(account.json())

        return account_list

    def update_account(self, change, client_id):
        sql = "UPDATE accounts SET balance=%s,atype=%s,astatus=%s WHERE account_id = %s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.balance, change.acc_type, change.acc_status, change.account_id))
        connection.commit()

        record = cursor.fetchone()

        if record:
            new_account = Account(record[0], record[1], record[2], float(record[3]), record[4], record[5])
            return new_account
        else:
            UserNotFound(f"Account with id: {client_id} - Not Found")

    def delete_account(self, account_id, client_id):
        sql = "DELETE FROM accounts WHERE account_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()
