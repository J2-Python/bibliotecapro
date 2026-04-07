from ast import Try
import json
from django.core.exceptions import ImproperlyConfigured
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

#! la carpeta base esta a 3 niveles arriba
BASE_DIR = Path(__file__).resolve().parent.parent.parent



with open("secrets.json") as f :
    secrets=json.loads(f.read())

def get_secret(secret_field,secrets=secrets):
    try:
        return secrets[secret_field]
    except KeyError:
        msg='la variable %s no existe' % secret_field
        raise ImproperlyConfigured(msg)
    
# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-u1thyurk5g@%r=up_pyvm30t3u@l6_macv6&37e%9#r3$&d)hb'
SECRET_KEY = get_secret('SECRET_KEY')

DJANGO_APPS=('django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',)
#! applications esta al mimo nivel de manage.py o sea en la raiz del proyecto
LOCAL_APPS=('applications.libro','applications.prestamo',)
THIRD_PARTY_APPS=('rest_framework',)

#CONCATENAMOS LAS APLICACIONES
INSTALLED_APPS = DJANGO_APPS+LOCAL_APPS+THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bibliotecapro.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bibliotecapro.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'