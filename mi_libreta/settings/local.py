from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':  'db_libreta',
        'USER': 'aldemar',
        'PASSWORD': '1qazxsw2',
        'PORT': '5432',
        'HOST': '127.0.0.1',
    }
}

