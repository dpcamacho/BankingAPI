from flask import jsonify, request

from exceptions.user_not_found import UserNotFound
from models.client import Client
from services.client_services import ClientServices


def route(app):
    @app.route("/clients", methods=['GET'])
    def get_all_clients():
        return jsonify(ClientServices.all_clients()), 200

    @app.route("/clients/<client_id>", methods=['GET'])
    def get_client(client_id):
        try:
            client = ClientServices.get_client_by_id(client_id)
            if client:
                return jsonify(client.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400
        except UserNotFound as r:
            return "No such client exists", 404

    @app.route("/clients", methods=['POST'])
    def post_client():
        client = Client.json_parse(request.json)
        client = ClientServices.create_client(client)

        return jsonify(client.json()), 201

    @app.route("/clients/<client_id>", methods=['PUT'])
    def put_client(client_id):
        try:
            client = Client.json_parse(request.json)
            client.client_id = int(client_id)
            client = ClientServices.update_client(client, client_id)

            return jsonify(client.json()), 200
        except UserNotFound as e:
            return "No such client exists", 404

    @app.route("/clients/<client_id>", methods=['DELETE'])
    def del_client(client_id):
        if ClientServices.delete_client(int(client_id)):
            return '', 204
        else:
            return "No such client exists", 404
