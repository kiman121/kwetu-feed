import secrets
import os

class Config:
    # FLASK_APP = os.environ('FLASK_APP')
    SECRET_KEY = secrets.token_hex(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos/users'

class ProdConfig(Config):
    # DATABASE = ""
    # POSTGRES_USER = ""
    # POSTGRES_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI= os.environ.get("SQL_URL")

class StagConfig(Config):
    DATABASE = ""
    POSTGRES_USER = ""
    POSTGRES_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = ""

class DevConfig(Config):
    FLASK_ENV = os.environ.get("FLASK_ENV")
    DATABASE = os.environ.get("DATABASE")
    POSTGRES_USER = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    # DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}


