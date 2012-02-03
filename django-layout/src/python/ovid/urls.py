# -*- coding: utf-8 -*-

from django.conf.urls.defaults import handler404, patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from @ovid@.signals import initialized

handler404 = '@ovid@.views.custom404'

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('userena.urls')),
)

urlpatterns += patterns('@ovid@.views',
    url(r'^$', 'index', name='@ovid@_index'),
)

def on_initialized(sender, **kwargs):
    pass

initialized.connect(on_initialized)
initialized.send(sender=None)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
