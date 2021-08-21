from flask import Flask
from configs.base_config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
photos = UploadSet('photos', IMAGES)

def create_app(config_name):
    '''
    Function that creates a instance of the app on run
    Args:
        config_name: configuration setting (development,production or test)
    '''
    app = Flask(__name__)
    # Set the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing Flask Extensions
    db.init_app(app)
    login_manager.init_app(app)

    # configure UploadSet
    configure_uploads(app, photos)

    # Register blue prints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')
   

    return app