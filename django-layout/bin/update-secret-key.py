# -*- coding: utf-8 -*-

import os
import random
import sys

try:
    settings_py = sys.argv[1]
except:
    print 'Usage: %s path/to/settings.py' % \
        (os.path.basename(sys.argv[0]))
    sys.exit(1)

CHARSET = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
SECRET_KEY = ''.join([random.choice(CHARSET) for i in range(50)])

lines = []
with open(settings_py, 'r') as fd:
    lines = fd.readlines()

with open(settings_py, 'w') as fd:
    for line in lines:
        if line.startswith('SECRET_KEY'):
            line = "SECRET_KEY = '%s'\n" % (SECRET_KEY)
        fd.write(line)

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
