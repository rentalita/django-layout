# -*- coding: utf-8 -*-

from django.contrib.auth.models import User

from userena.models import UserenaLanguageBaseProfile


class Profile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(User, unique=True,
                                related_name=u'profile')

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
