# -*- coding: utf-8 -*-

from django.conf.urls.defaults import handler404, patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

handler404 = '@ovid@.views.custom404'

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('@ovid@.views',
    url(r'^$', 'index'),
)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
