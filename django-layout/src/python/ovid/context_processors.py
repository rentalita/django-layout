# -*- coding: utf-8 -*-

from django.conf import settings


def maintenance_mode(request):
    return {'MAINTENANCE_MODE': settings.MAINTENANCE_MODE}

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
