#!/bin/sh

@OVID@_HOME="$(dirname $0)"/..
export @OVID@_HOME

. "${@OVID@_HOME}"/etc/common

FILENAME="$1"

if [ "${FILENAME}" = "" ]; then
    FILENAME="${@OVID@_DATA}"/django-load.json
fi

"${@OVID@_BIN}"/django-manage.sh loaddata "${FILENAME}"

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
