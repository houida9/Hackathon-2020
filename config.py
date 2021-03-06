import os

# Create dummy secrey key so we can use sessions
SECRET_KEY = os.environ.get('SECRET_KEY')

# Create in-memory database
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_ECHO = True

# Flask-Security config
SECURITY_URL_PREFIX = os.environ.get('SECURITY_URL_PREFIX')
SECURITY_PASSWORD_HASH = os.environ.get('SECURITY_PASSWORD_HASH')
SECURITY_PASSWORD_SALT = os.environ.get('SECURITY_PASSWORD_SALT')

# Flask-Security URLs, overridden because they don't put a / at the end
SECURITY_LOGIN_URL = os.environ.get('SECURITY_LOGIN_URL')
SECURITY_LOGOUT_URL = os.environ.get('SECURITY_LOGOUT_URL')
SECURITY_REGISTER_URL = os.environ.get('SECURITY_REGISTER_URL')

SECURITY_POST_LOGIN_VIEW = os.environ.get('SECURITY_POST_LOGIN_VIEW')
SECURITY_POST_LOGOUT_VIEW = os.environ.get('SECURITY_POST_LOGOUT_VIEW')
SECURITY_POST_REGISTER_VIEW = os.environ.get('SECURITY_POST_REGISTER_VIEW')

# Flask-Security features
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
