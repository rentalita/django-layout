# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models

from userena.models import UserenaLanguageBaseProfile


class Profile(UserenaLanguageBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=u'user',
                                related_name=u'profile')

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
