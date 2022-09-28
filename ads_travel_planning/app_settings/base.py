from typing import Any


class BaseSettings:
    allowed_hosts = list()
    debug = False
    db_host = ''
    db_port = ''

    def __init__(self, env: Any):
        self.env = env

    @property
    def secret_key(self):
        return self.env.str('SECRET_KEY', '')

    @property
    def db_name(self):
        return self.env.str('DB_NAME', '')

    @property
    def db_user(self):
        return self.env.str('DB_USER', '')

    @property
    def db_password(self):
        return self.env.str('DB_PASSWORD', '')

