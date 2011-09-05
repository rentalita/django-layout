# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

import @ovid@.urls

urlpatterns = patterns('',
    url(r'^@ovid@/', include(@ovid@.urls)),
)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
