from flask import Flask
from flask_restful import Api
from jwt import ExpiredSignatureError
from werkzeug.exceptions import HTTPException

from config.config import config_app
from route.app_v0 import config_routes_v0
from utils.response_erro import ResponseErro

app = Flask(__name__)
api = Api(app)

api = config_app(api)
api = config_routes_v0(api)


@app.errorhandler(ExpiredSignatureError)
def handle_expired_signature_error(error):
    response = ResponseErro.token_expirado()
    response.status_code = getattr(error, 'code', 401)
    return response


@app.errorhandler(HTTPException)
def handle_http_exception(error):
    response = ResponseErro.http_exception()
    response.status_code = getattr(error, 'code', 500)
    return response


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
