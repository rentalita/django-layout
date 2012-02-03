# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, url

from . import tasks
from . import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='@ovid@_index'),
)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
