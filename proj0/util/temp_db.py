from models.client import Client


class TempDB:

    clients = {
        1: Client(client_id=1, name="danny", email="abc@gmail.com", password="abc"),
        2: Client(client_id=2, name="maddy", email="123@gmail.com", password="123"),
        3: Client(client_id=3, name="daniel", email="jkl@gmail.com", password="jkl")
    }