import os
import sys

path = '/home/your-username/ProjetoLocalizacaoGPS/backend'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'gps_tracker.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
