"""
WSGI config for dailyfresh project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append('C:/Blog/dailyfresh')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailyfresh.settings')

application = get_wsgi_application()
