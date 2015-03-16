import os
from pathlib import Path

from django.core.exceptions import ImproperlyConfigured

import dj_database_url


def get_env_variable(name):
    """ Gets the specified environment variable.

    :param name: The name of the variable.
    :type name: str
    :returns: The value of the specified variable.
    :raises: **ImproperlyConfigured** when the specified variable does not exist.

    """

    try:
        return os.environ[name]
    except KeyError:
        error_msg = "The %s environment variable is not set!" % name
        raise ImproperlyConfigured(error_msg)


# ======================================================================================================== #
#                                         General Management                                               #
# ======================================================================================================== #

ADMINS = (
    ('Alex Kavanaugh', 'kavanaugh.development@outlook.com'),
    ('Arnav Murulidhar', 'murulidhar@yahoo.com'),
    ('Matthew Morris', 'matmo10@gmail.com')
)

MANAGERS = ADMINS

# ======================================================================================================== #
#                                         General Settings                                                 #
# ======================================================================================================== #

# Local time zone for this installation. Choices can be found here:
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation.
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

DATE_FORMAT = 'l, F d, Y'

TIME_FORMAT = 'h:i a'

DATETIME_FORMAT = 'l, F d, Y h:i a'

DEFAULT_CHARSET = 'utf-8'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

ROOT_URLCONF = 'catroulette.urls'

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# ======================================================================================================== #
#                                          Database Configuration                                          #
# ======================================================================================================== #

DATABASES = {
    'default': dj_database_url.config(default=get_env_variable('CAT_DATABASE_URL')),
}

# ======================================================================================================== #
#                                        Authentication Configuration                                      #
# ======================================================================================================== #

AUTH_USER_MODEL = 'core.CatRouletteCat'

# ======================================================================================================== #
#                                      Session/Security Configuration                                      #
# ======================================================================================================== #

# Cookie settings.
SESSION_COOKIE_HTTPONLY = True

# Session expiraton
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = get_env_variable('CAT_SECRET_KEY')

# ======================================================================================================== #
#                                  File/Application Handling Configuration                                 #
# ======================================================================================================== #

PROJECT_DIR = Path(__file__).parents[2]

# The directory that will hold user-uploaded files.
MEDIA_ROOT = str(PROJECT_DIR.joinpath("media").resolve())

# URL that handles the media served from MEDIA_ROOT. Make sure to use a trailing slash.
MEDIA_URL = '/media/'

# The directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
STATIC_ROOT = str(PROJECT_DIR.joinpath("static").resolve())

# URL prefix for static files. Make sure to use a trailing slash.
STATIC_URL = '/static/'

STATIC_PRECOMPILER_OUTPUT_DIR = ""
STATIC_PRECOMPILER_DISABLE_AUTO_COMPILE = True

# Additional locations of static files
STATICFILES_DIRS = (
    str(PROJECT_DIR.joinpath("catroulette", "static").resolve()),
)

# List of finder classes that know how to find static files in various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'static_precompiler.finders.StaticPrecompilerFinder',
)

TEMPLATE_DIRS = (
    str(PROJECT_DIR.joinpath("catroulette", "templates").resolve()),
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

# List of processors used by RequestContext to populate the context.
# Each one should be a callable that takes the request object as its
# only parameter and returns a dictionary to add to the context.
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'raven.contrib.django.raven_compat.middleware.SentryResponseErrorIdMiddleware',
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'raven.contrib.django.raven_compat',
    'django_ajax',
    'dj_database_url',
    'static_precompiler',
    'catroulette.apps.core',
)

# ======================================================================================================== #
#                                       REST Endpoint Configuration                                        #
# ======================================================================================================== #

CORS_ORIGIN_ALLOW_ALL = True

# ======================================================================================================== #
#                                         Logging Configuration                                            #
# ======================================================================================================== #

RAVEN_CONFIG = {
    'dsn': get_env_variable('CAT_SENTRY_DSN'),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'INFO',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'INFO',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'django_ajax': {
            'level': 'INFO',
            'handlers': ['sentry'],
            'propagate': True,
        },
    }
}

