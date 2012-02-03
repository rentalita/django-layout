# -*- coding: utf-8 -*-

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'default/index.html'

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
