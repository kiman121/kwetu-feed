from flask import Flask
from configs.base_config import config_options



def create_app(config_name):
    app = Flask(__name__)
    # Set the app configurations
    app.config.from_object(config_options[config_name])

    # Register blue prints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)





    return app