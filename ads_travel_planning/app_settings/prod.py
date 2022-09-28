from ads_travel_planning.app_settings.base import BaseSettings
from utils.singleton import Singleton


class AppSettings(Singleton, BaseSettings):
    allowed_hosts = list()
    debug = False
    env = dict()
    db_host = ''
    db_port = ''
