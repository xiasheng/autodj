
import os,sys

os.environ['DJANGO_SETTINGS_MODULE']='dj_demo.settings'

path = '/var/www/dj_demo'
if path not in sys.path:
        sys.path.append(path)

import django.core.handlers.wsgi

application=django.core.handlers.wsgi.WSGIHandler()

