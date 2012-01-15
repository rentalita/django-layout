# -*- coding: utf-8 -*-

from functools import wraps

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext


def render_to_response_with_context_instance(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        response = view(request, *args, **kwargs)
        if type(response) == HttpResponse:
            return response
        template, kwargs = response
        kwargs['context_instance'] = RequestContext(request)
        return render_to_response(template, **kwargs)
    return wrapper

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
