#!/usr/bin/env python

from django.core.handlers.wsgi import WSGIHandler
from flup.server.fcgi import WSGIServer


WSGIServer(WSGIHandler()).run()

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
