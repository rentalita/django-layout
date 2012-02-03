# -*- coding: utf-8 -*-

import os

import django.conf.global_settings as DEFAULT_SETTINGS

gettext = lambda s: s

ADMINS = (
    ('Crash Reports', 'crash-reports@@ovid@.com'),
)

DEFAULT_FROM_EMAIL = '@Ovid@ <no-reply@@ovid@.com>'

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.environ['@OVID@_DB'] + os.sep + '@ovid@.db',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', u'English'),
    ('es', u'Español'),
)

LOCALE_PATHS = DEFAULT_SETTINGS.LOCALE_PATHS + (
    os.environ['@OVID@_HOME'] + os.sep + 'locale',
)

MEDIA_ROOT = os.environ['@OVID@_WWW'] + os.sep + 'media'

APPEND_SLASH = False
FORCE_SCRIPT_NAME = ''

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/admin-media/'

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY =

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    '@ovid@.context_processors.maintenance_mode',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.gzip.GZipMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = '@ovid@.urls'

TEMPLATE_DIRS = (
    os.environ['@OVID@_WWW'] + '/templates/',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'easy_thumbnails',
    'guardian',
    'south',
    'userena',
    'tastypie',
)

INSTALLED_APPS += (
    '@ovid@.default',
    '@ovid@.profile',
)

ANONYMOUS_USER_ID = -1

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
AUTH_PROFILE_MODULE = 'profile.Profile'

USERENA_DEFAULT_PRIVACY = 'closed'
USERENA_DISABLE_PROFILE_LIST = True
USERENA_REMEMBER_ME_DAYS = (gettext('a very long time'), 1024)
USERENA_USE_HTTPS = True
USERENA_USE_MESSAGES = False
USERENA_WITHOUT_USERNAMES = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        '@ovid@_log': {
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': os.environ['@OVID@_LOG'] + os.sep + '@ovid@.log',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins', '@ovid@_log'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django': {
            'handlers': ['mail_admins', '@ovid@_log'],
            'level': 'ERROR',
            'propagate': True,
        },
        'ldnlrd': {
            'handlers': ['mail_admins', '@ovid@_log'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
