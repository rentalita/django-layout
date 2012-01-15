# -*- coding: utf-8 -*-

from @ovid@.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

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

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
