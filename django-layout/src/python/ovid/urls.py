# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from @ovid@.signals import initialized

urlpatterns = patterns('',
    url(r'^accounts/', include('userena.urls')),
)

urlpatterns += patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('@ovid@.default.urls')),
)

def on_initialized(sender, **kwargs):
    pass

initialized.connect(on_initialized)
initialized.send(sender=None)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
