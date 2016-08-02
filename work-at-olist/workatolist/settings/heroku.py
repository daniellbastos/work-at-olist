from prettyconf import config
import dj_database_url

from workatolist.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['work-at-list.herokuapp.com']

DATABASES = {
    'default': dj_database_url.parse(config('DATABASE_URL'))
}

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
