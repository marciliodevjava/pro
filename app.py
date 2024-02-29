from flask import Flask
from flask_restful import Api

from route.app_v0 import config_routes_v0

app = Flask(__name__)
api = Api(app)

api = config_routes_v0(api)

if __name__ == "__main__":
    app.run(debug=False)
