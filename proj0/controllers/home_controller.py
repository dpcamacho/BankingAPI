
def route(app):
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        return "Hello. Welcome to Open Financial!"

    @app.route("/contact")
    def contact():
        return "Contact us via email: OpenFinancial@gmail.com"
