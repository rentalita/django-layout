# -*- coding: utf-8 -*-

from functools import wraps

from django.template import RequestContext
from django.shortcuts import render_to_response


def render_to_response_with_context_instance(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        return render_to_response(*view(request, *args, **kwargs),
                                   context_instance=RequestContext(request))
    return wrapper

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
