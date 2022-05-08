from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options


bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask (__name__)

    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)

    from.main import main as main_Blueprint
    app.register_blueprint(main_Blueprint)




    return app
