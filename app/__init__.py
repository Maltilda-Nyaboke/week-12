from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail


db= SQLAlchemy()
mail = Mail()
photos = UploadSet('photos',IMAGES)
bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask (__name__)

    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    configure_uploads(app,photos)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    
    from.main import main as main_Blueprint
    app.register_blueprint(main_Blueprint)





    return app
