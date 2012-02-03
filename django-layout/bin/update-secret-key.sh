#!/bin/sh

@OVID@_HOME="$(dirname $0)"/..
export @OVID@_HOME

. "${@OVID@_HOME}"/etc/common

"${@OVID@_BIN}"/python.sh "${@OVID@_BIN}"/update-secret-key.py "${@OVID@_SRC}"/python/@ovid@/settings.py

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
