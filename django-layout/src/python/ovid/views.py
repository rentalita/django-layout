# -*- coding: utf-8 -*-

from django.views.decorators.http import require_http_methods

from @ovid@.utils.decorators import \
    render_to_response_with_context_instance


@require_http_methods(['GET'])
@render_to_response_with_context_instance
def index(request):
    return ('@ovid@-index.tmpl.%s' % (request.LANGUAGE_CODE),)


@require_http_methods(['GET'])
@render_to_response_with_context_instance
def custom404(request):
    try:
        custom404_tmpl = settings.@OVID@_CUSTOM404_TEMPLATE
    except:
        custom404_tmpl = '@ovid@-custom404.tmpl.%s'

    return (custom404_tmpl % (request.LANGUAGE_CODE),)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
