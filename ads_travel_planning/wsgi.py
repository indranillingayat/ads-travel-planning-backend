import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ads_travel_planning.settings')

application = get_wsgi_application()
