# -*- coding: utf-8 -*-

from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, 'default/index.html')

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
