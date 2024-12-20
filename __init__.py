# init.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app