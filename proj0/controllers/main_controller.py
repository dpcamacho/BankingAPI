from controllers import home_controller, client_controller, account_controller


def route(app):

    home_controller.route(app)
    client_controller.route(app)
    account_controller.route(app)
