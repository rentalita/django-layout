#!/bin/sh -e

@OVID@_HOME="$(dirname $0)"/..
export @OVID@_HOME

. "${@OVID@_HOME}"/etc/common

TARGET="$@"
TARGET="${TARGET:-help}"

"${@OVID@_BIN}"/python.sh "${@OVID@_BIN}"/django-manage.py ${TARGET} --settings="${DJANGO_SETTINGS_MODULE}" -v 0

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
