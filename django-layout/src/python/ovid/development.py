# -*- coding: utf-8 -*-

from @ovid@.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

DEFAULT_FROM_EMAIL = 'webmaster@localhost'

MAINTENANCE_MODE = 'DEVELOPMENT'

EMAIL_PORT = 1025

INSTALLED_APPS += (
    'debug_toolbar',
    )

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

INTERNAL_IPS = (
    '127.0.0.1',
    )

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
