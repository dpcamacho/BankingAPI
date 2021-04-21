from daos.client_dao import ClientDAO
from exceptions.user_not_found import UserNotFound
from models.client import Client
from util.db_connection import connection


class ClientDAOImpl(ClientDAO):

    def create_client(self, client):
        sql = "INSERT INTO clients VALUES (DEFAULT,%s,%s,%s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (client.name, client.email, client.password))

        connection.commit()
        record = cursor.fetchone()

        new_client = Client(record[0], record[1], record[2], record[3])
        return new_client

    def get_client(self, client_id):
        sql = "SELECT * FROM clients WHERE client_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])

        record = cursor.fetchone()
        if record:
            return Client(record[0], record[1], record[2], record[3])
        else:
            raise UserNotFound(f"Client with id: {client_id} - Not Found")

    def all_clients(self):
        sql = "SELECT * FROM clients"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        client_list = []
        for record in records:
            client = Client(record[0], record[1], record[2], record[3])
            client_list.append(client.json())

        return client_list

    def update_client(self, change, client_id):
        sql = "UPDATE clients SET client_name=%s, email=%s, client_pw=%s WHERE client_id=%s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (change.name, change.email, change.password, change.client_id))

        record = cursor.fetchone()

        if record:
            new_client = Client(record[0], record[1], record[2], record[3])
            return new_client
        else:
            raise UserNotFound(f"Client with id: {client_id} - Not Found")

    def delete_client(self, client_id):
        sql = "DELETE FROM clients WHERE client_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        connection.commit()
