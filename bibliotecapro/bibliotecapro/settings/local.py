
#! incluimos todo lo del archivo base
from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': BASE_DIR / 'db.sqlite3',
        
        'NAME': get_secret('NAME'),
        'USER':get_secret('USER'),
        'PASSWORD':get_secret('PASSWORD'),
        'HOST':get_secret('HOST'),
        'PORT':get_secret('PORT')
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'