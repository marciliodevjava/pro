from flask import Flask
from flask_restful import Api

from config.config import config_app
from route.app_v0 import config_routes_v0

app = Flask(__name__)
api = Api(app)

api = config_app(api)

api = config_routes_v0(api)

if __name__ == "__main__":
    app.run(debug=False)
