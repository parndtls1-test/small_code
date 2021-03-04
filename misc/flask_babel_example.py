from flask import Flask, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

@babel.localepythselector
def get_locale():
    x = request.accept_languages.best_match(['en','es','de'])
    print(x)

get_locale()
