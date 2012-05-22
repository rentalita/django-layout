#!/usr/bin/env python

import os

from django.core.handlers.wsgi import WSGIHandler
from flup.server.fcgi import WSGIServer


os.environ['CELERY_LOADER'] = 'django'

WSGIServer(WSGIHandler()).run()

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
