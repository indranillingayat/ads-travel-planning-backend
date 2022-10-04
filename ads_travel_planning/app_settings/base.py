import os


class BaseSettings:
    allowed_hosts = list()
    debug = False
    db_host = ''
    db_port = ''

    @property
    def secret_key(self):
        return os.environ.get('SECRET_KEY', 'junk')

    @property
    def db_name(self):
        return os.environ.get('DB_NAME', '')

    @property
    def db_user(self):
        return os.environ.get('DB_USER', '')

    @property
    def db_password(self):
        return os.environ.get('DB_PASSWORD', '')

