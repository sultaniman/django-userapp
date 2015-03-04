import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '#8=_m#k=$-f@@b(hr8a29bp-$ubllmlep9e=lld2#gb%ugdogp'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ["*"]
USERAPP_ID = "FAKE_ID"

INSTALLED_APPS = (
    'django_userapp',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
)

ROOT_URLCONF = 'test_project.urls'
WSGI_APPLICATION = 'test_project.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'