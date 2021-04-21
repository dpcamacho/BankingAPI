class Client:

    def __init__(self, client_id=0, name="", email="", password=""):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.password = password

    def json(self):
        return {
            'clientId': self.client_id,
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    @staticmethod
    def json_parse(json):
        client = Client()
        client.client_id = json["clientId"]
        client.name = json["name"]
        client.email = json["email"]
        client.password = json["password"]

        return client

    def __repr__(self):
        return str(self.json())
