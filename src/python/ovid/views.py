# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET'])
def index(request):
    return render_to_response('@ovid@-index.tmpl.%s' % (request.LANGUAGE_CODE))


@require_http_methods(['GET'])
def custom404(request):
    try:
        custom404_tmpl = settings.@OVID@_CUSTOM404_TEMPLATE
    except:
        custom404_tmpl = '@ovid@-custom404.tmpl.%s'

    return render_to_response(custom404_tmpl % (request.LANGUAGE_CODE))

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
