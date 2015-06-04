"""
Django settings for mati project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_rkv%(^+0fbw@^$er*h*5%d1g2sg30gavq@p+%gx&xwk*n24v5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_extensions',
    'proxy_server',
    'map',
    'dimaps',
    'rest_framework',
    'rest_framework.authtoken',
    'bootstrapform',
)
AUTH_USER_MODEl = 'map.Person'
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #operaciones de post y put seguridad de csrf no se genera el token csrf porque no se generan html
    'proxy_server.middleware.DisableCSRF',
)


ROOT_URLCONF = 'mati.urls'

WSGI_APPLICATION = 'mati.wsgi.application'

#URL for @login_required decorator to use
LOGIN_URL = '/accounts/login/'

#redirect authenticated users
LOGIN_REDIRECT_URL = '/accounts/loggedin/'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#user=matidb
#password = portalmatidimap
#'NAME': 'mati_db',
#'NAME': 'report_data',
#pip Django==1.6

# 'reports': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'db_k2',
#         'USER': 'postgres',
#         'PASSWORD': 'kelvin',
#         'HOST': 'localhost'
#     }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_k1',
        'USER': 'postgres',
        'PASSWORD': 'kelvin',
        'HOST': 'localhost',
    },

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

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/bootstrap'),
    os.path.join(BASE_DIR, 'static/jquery'),
    os.path.join(BASE_DIR, 'static/application'),
    os.path.join(BASE_DIR, 'static/font-awesome'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    os.path.join(BASE_DIR,  'templates'),
    os.path.join(BASE_DIR,  'templates/dimaps'),
    os.path.join(BASE_DIR,  'templates/dimaps/service'),
)

PROXY_API_KEYS = [
    # Add the API KEYS you wish to allow consuming services
    '^ugfp@+cw!+se1b8kw%!23(sbrzk8f!uzrhqp$s)@67g9f1tdj',
    '123'
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}

#DATABASE_ROUTERS = ['map.routers.CoordinatorRouter']

#AUTH_PROFILE_MODULE = 'map.Student'
# REST_FRAMEWORK = {
#     'PAGINATE_BY': 10,
# }