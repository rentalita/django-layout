# -*- coding: utf-8 -*-

from django.views.decorators.http import require_http_methods

from @ovid@.utils.decorators import \
    render_to_response_with_context_instance


@require_http_methods(['GET'])
@render_to_response_with_context_instance
def index(request):
    return ('@ovid@-index.html',)


@require_http_methods(['GET'])
@render_to_response_with_context_instance
def custom404(request):
    try:
        custom404_template = settings.@OVID@_CUSTOM404_TEMPLATE
    except:
        custom404_template = '@ovid@-custom404.html'

    return (custom404_template,)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
