import os


class BaseConfig(object):
    SECRET_KEY = 'CHAVE_SECRETA\-\-'
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DB_NAME = os.environ['DB_ENV_POSTGRES_USER']
    DB_USER = os.environ['DB_ENV_POSTGRES_USER']
    DB_PASS = os.environ['DB_ENV_POSTGRES_PASSWORD']
    DB_PORT = os.environ['DB_PORT_5432_TCP_PORT']
    DB_SERVICE = os.environ['DB_PORT_5432_TCP_ADDR']
    DB_URL = "postgresql://{user}:{passwd}@{address}:{port}/{name}"
    SQLALCHEMY_DATABASE_URI = DB_URL.format(
                user=DB_USER,
                passwd=DB_PASS,
                address=DB_SERVICE,
                port=DB_PORT,
                name=DB_NAME
            )

    # DB_NAME = 'postgress'
    # DB_USER = 'postgress'
    # DB_PASS = '123'
    # DB_SERVICE = '172.17.0.2'

    #DB_PORT = 5432
    # SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
    #     DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    # )