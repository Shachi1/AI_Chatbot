from os import environ

APPLICATION_ENV = environ.get('APPLICATION_ENV') or 'development'
SECRET_KEY = environ.get('SECRET_KEY')
APP_NAME = environ.get('APP_NAME')
OPENAI_API_KEY = environ.get('OPENAI_API_KEY')
# API_KEY = environ.get('API_KEY')
# BROKER_URL = environ.get('BROKER_URL')
# RESULT_BACKEND = environ.get('RESULT_BACKEND')
# DATABASE_URL = environ.get('DATABASE_URL')
# SECRET_KEY = environ.get('SECRET_KEY')
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
