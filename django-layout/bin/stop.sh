#!/bin/sh -e

@OVID@_HOME="$(dirname $0)"/..
export @OVID@_HOME

. "${@OVID@_HOME}"/etc/common

"${@OVID@_BIN}"/lighttpd.sh stop
"${@OVID@_BIN}"/celeryd.sh stop

exit 0

# Local Variables:
# indent-tabs-mode: nil
# End:
# vim: ai et sw=4 ts=4
