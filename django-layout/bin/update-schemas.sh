#!/bin/sh

@OVID@_HOME="$(dirname $0)"/..
export @OVID@_HOME

. "${@OVID@_HOME}"/etc/common

"${@OVID@_BIN}"/django-manage.sh schemamigration @ovid@ --auto

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
