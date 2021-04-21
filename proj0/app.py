from flask import Flask, jsonify

from logger import log
from controllers import main_controller as mc

app = Flask(__name__)

mc.route(app)
log()

if __name__ == '__main__':
    app.run(debug=True)
