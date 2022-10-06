from ads_travel_planning.app_settings.base import BaseSettings
from utils.singleton import Singleton


class AppSettings(Singleton, BaseSettings):
    allowed_hosts = ['127.0.0.1', 'localhost']
    debug = False
    db_host = 'ads-test-database.c13lsk8zdesp.us-east-1.rds.amazonaws.com'
    db_port = 5432
    logging_enabled = False
