"""
Django settings for jet_demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

try:
    from configparser import RawConfigParser
except ImportError:
    from ConfigParser import RawConfigParser
import os
from django.conf import global_settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

# Config

config = RawConfigParser()

PROJECT_NAME = 'jet_demo'

production_config = os.path.join('/usr/local/etc', PROJECT_NAME, '{0}.conf'.format(PROJECT_NAME))
development_config = os.path.join(BASE_DIR, 'conf', '{0}.conf'.format(PROJECT_NAME))

config_path = production_config if os.path.exists(production_config) else development_config
config.read(config_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get('common', 'secret_key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config.getboolean('common', 'debug')

TEMPLATE_DEBUG = config.getboolean('common', 'debug')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'jet.dashboard',
    'jet',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'adminsortable2',
    'mptt',
    'ckeditor',
    'tinymce',
    'debug_toolbar',
    'core',
    'people',
    'menu',
    'editors',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
)

TEMPLATE_DIRS = (
    'core/templates',
)

ROOT_URLCONF = 'application.urls'

WSGI_APPLICATION = 'application.wsgi.application'

# E-mail

SERVER_EMAIL = config.get('email', 'server_email')
ADMINS = ()
MANAGERS = ()

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = config.get('email', 'host')
EMAIL_PORT = config.get('email', 'port')
EMAIL_HOST_USER = config.get('email', 'user')
EMAIL_HOST_PASSWORD = config.get('email', 'password')
EMAIL_USE_TLS = config.getboolean('email', 'tls')

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config.get('database', 'ENGINE'),
        'NAME': config.get('database', 'NAME'),
        'USER': config.get('database', 'USER'),
        'PASSWORD': config.get('database', 'PASSWORD'),
        'HOST': config.get('database', 'HOST'),
        'PORT': config.get('database', 'PORT'),
        'OPTIONS': {'charset': 'utf8', },
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR, 'static', 'media')

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['mail_admins'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}

# Django JET

JET_DEFAULT_THEME = 'default'
JET_THEMES = [
    {
        'theme': 'default',
        'color': '#47bac1',
        'title': 'Default'
    },
    {
        'theme': 'green',
        'color': '#44b78b',
        'title': 'Green'
    },
    {
        'theme': 'light-green',
        'color': '#2faa60',
        'title': 'Light Green'
    },
    {
        'theme': 'light-violet',
        'color': '#a464c4',
        'title': 'Light Violet'
    },
    {
        'theme': 'light-blue',
        'color': '#5EADDE',
        'title': 'Light Blue'
    },
    {
        'theme': 'light-gray',
        'color': '#222',
        'title': 'Light Gray'
    }
]
JET_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
JET_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'

JET_MODULE_YANDEX_METRIKA_CLIENT_ID = '46de85bff0f94c82bbf42be177f128a2'
JET_MODULE_YANDEX_METRIKA_CLIENT_SECRET = '01107ac1049b49ab9b24e60e95ba2a93'
JET_MODULE_GOOGLE_ANALYTICS_CLIENT_SECRETS_FILE = os.path.join(PROJECT_DIR, 'client_secrets.json')

# CKEditor

CKEDITOR_UPLOAD_PATH = 'uploads/'
