# Set this to the same path you used in settings.py, or None ('') for auto-detection.
SNAKE_CMS_ROOT = ''

### DO NOT CHANGE ANYTHING BELOW THIS LINE ###

import os, sys
from os.path import join, dirname, abspath, exists

# Path auto-detection
if not SNAKE_CMS_ROOT or not exists( SNAKE_CMS_ROOT ):
        SNAKE_CMS_ROOT = dirname(abspath(__file__))

# environment variables
sys.path.append( SNAKE_CMS_ROOT )
sys.path.append( join( SNAKE_CMS_ROOT, 'cms' ) )
sys.path.append( join( SNAKE_CMS_ROOT, 'snakelog' ) )
os.environ['DJANGO_SETTINGS_MODULE'] = 'cms.settings'

# If you get an error about Python not being able to write to the Python
# egg cache, the egg cache path might be set awkwardly. This should not
# happen under normal circumstances, but every now and then, it does.
# Uncomment this line to point the egg cache to /tmp.
#os.environ['PYTHON_EGG_CACHE'] = '/tmp/pyeggs'

# WSGI handler
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()