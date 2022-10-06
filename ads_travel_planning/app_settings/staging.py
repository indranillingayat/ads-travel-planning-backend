from ads_travel_planning.app_settings.base import BaseSettings
from utils.singleton import Singleton


class AppSettings(Singleton, BaseSettings):
    db_host = 'ads-test-database.c13lsk8zdesp.us-east-1.rds.amazonaws.com'
    db_port = 5432
    allowed_hosts = ['adstravelplannerstaging-env.eba-fpbsp8bs.us-east-1.elasticbeanstalk.com',
                     'staging-travel-planner.adsba-test.com']
