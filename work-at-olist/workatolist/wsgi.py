"""
WSGI config for workatolist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from prettyconf import config

settings = config('SETTINGS', default='workatolist.settings.local')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings)

application = get_wsgi_application()
